"""
Todos os números do dashboard vêm daqui. As premissas ficam em data/premissas.json
e os equipamentos em data/equipamentos.csv.
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd


# CONFIGURAÇÕES 
RAIZ = Path(__file__).resolve().parent.parent

DIAS_MES = 30
ANOS = 10

# Perfil mensal sintético de horas de sol pleno.
HSP_MENSAL = [
    5.2, 5.2, 4.7, 4.5,
    3.9, 3.6, 3.8, 4.3,
    4.2, 4.6, 5.0, 5.2
]

# CRREGAMENTO DOS DADOS
def carregar_premissas():
    """Carrega as premissas do arquivo JSON."""

    caminho = RAIZ / "data" / "premissas.json"

    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_equipamentos():
    """Carrega a tabela de equipamentos do arquivo CSV."""

    caminho = RAIZ / "data" / "equipamentos.csv"

    return pd.read_csv(caminho)


# CÁLCULO  CONSUMO ENERGÉTICO
def consumo(equip: pd.DataFrame):
    """
    Calcula o consumo energético dos equipamentos.

    Fórmula:
    E = (quantidade x potência x horas) / 1000

    Resultado em kWh.
    """

    df = equip.copy()

    df["wh_dia"] = (
        df["quantidade"]
        * df["potencia_w"]
        * df["horas_dia"]
    )

    df["kwh_mes"] = (
        df["wh_dia"] * DIAS_MES / 1000
    )

    df["kwh_ano"] = (
        df["wh_dia"] * 365 / 1000
    )

    total_wh = df["wh_dia"].sum()

    resultado = {
        "wh_dia": total_wh,
        "kwh_dia": total_wh / 1000,
        "kwh_mes": total_wh * DIAS_MES / 1000,
        "kwh_ano": total_wh * 365 / 1000,
    }

    return df, resultado



# TARIFA DE ENERGIA ELÉTRICA
def tarifa_com_tributos(p):
    """
    Calcula a tarifa com tributos.

    A tarifa informada no arquivo de premissas não inclui
    ICMS e PIS/COFINS.
    """

    aliquotas = p["icms"] + p["pis_cofins"]

    if aliquotas >= 1:
        raise ValueError(
            "A soma das alíquotas de tributos deve ser menor que 1."
        )

    return (
        p["tarifa_enel_sem_tributos_kwh"]
        / (1 - aliquotas)
    )


# DIMENSIONAMENTO  SISTEMA SOLAR
def dimensionar_solar(wh_dia, p):
    """
    Dimensiona a potência mínima do painel e a capacidade
    mínima da bateria.

    Considera:
    - Horas de sol pleno;
    - Desempenho global do sistema;
    - Autonomia desejada;
    - Profundidade de descarga da bateria.
    """

    if wh_dia <= 0:
        raise ValueError(
            "O consumo diário deve ser maior que zero."
        )

    # Potência mínima do painel solar
    pot_minima = (
        wh_dia
        / (
            p["hsp_projeto"]
            * p["desempenho_global_pr"]
        )
    )

    # Capacidade mínima da bateria em Wh
    cap_wh_min = (
        wh_dia
        * p["autonomia_alvo_dias"]
        / p["dod_lifepo4"]
    )

    # Capacidade mínima da bateria em Ah
    ah_min = (
        cap_wh_min
        / p["tensao_bateria_v"]
    )

    # Capacidade da bateria adotada
    cap_wh = (
        p["bateria_ah"]
        * p["tensao_bateria_v"]
    )

    # Autonomia real da bateria adotada
    autonomia = (
        cap_wh
        * p["dod_lifepo4"]
        / wh_dia
    )

    # Geração média estimada
    ger_media = (
        p["painel_wp"]
        * p["hsp_media_anual"]
        * p["desempenho_global_pr"]
    )

    # Geração estimada no cenário de projeto
    ger_pior = (
        p["painel_wp"]
        * p["hsp_projeto"]
        * p["desempenho_global_pr"]
    )

    return {
        "painel_minimo_wp": pot_minima,
        "bateria_minima_ah": ah_min,
        "bateria_wh": cap_wh,
        "autonomia_dias": autonomia,
        "geracao_media_wh_dia": ger_media,
        "geracao_pior_mes_wh_dia": ger_pior,
        "folga_pior_mes": (
            ger_pior / wh_dia - 1
        ),
    }


# COMPARAÇÃO FINANCEIRA
def comparar(p, c):
    """
    Compara:
    A  - Nova ligação à rede elétrica.
    A2 - Ponto existente, com extensão do circuito.
    B  - Sistema solar com bateria.

    Separa investimento inicial (CAPEX), contas,
    manutenção e custo total de propriedade (TCO).
    """

    # ALTERNATIVA A — REDE ELÉTRICA
    tarifa = tarifa_com_tributos(p)

    kwh_faturado = max(
        c["kwh_mes"],
        p["custo_disponibilidade_kwh_mes"]
    )

    conta_mes = round(kwh_faturado * tarifa, 2)

    capex_a = (
        p["investimento_rede_instalacao"]
        + p["investimento_rede_equipamentos"]
        + p["investimento_rede_documentacao"]
    )

    # ALTERNATIVA A2 — PONTO EXISTENTE
    capex_a_extensao = p["custo_circuito_interno"]

    # ALTERNATIVA B — ENERGIA SOLAR
    custo_paineis = (
        p["quantidade_paineis"]
        * p["custo_unitario_painel"]
    )

    capex_b_base = (
        custo_paineis
        + p["custo_bateria"]
        + p["custo_controlador_mppt"]
        + p["custo_bos"]
        + p["custo_mao_obra_solar"]
        + p["documentacao_solar"]
    )

    reserva_solar = p["reserva_adequacao_solar"]
    capex_b = capex_b_base + reserva_solar

    conta_solar_mes = p["conta_solar_mensal"]

    manutencao_b_ano = p["manutencao_solar_ano"]
    manutencao_b_mes = manutencao_b_ano / 12

    custo_operacional_solar_mes = (
        conta_solar_mes + manutencao_b_mes
    )

    economia_mes = conta_mes - custo_operacional_solar_mes

    diferenca_investimento = capex_b - capex_a

    # PROJEÇÃO FINANCEIRA DE 10 ANOS
    anos = np.arange(0, ANOS + 1)
    reajuste = p["reajuste_tarifa_aa"]

    conta_ano = np.array([
        conta_mes * 12 * (1 + reajuste) ** (ano - 1)
        if ano > 0 else 0
        for ano in anos
    ])

    conta_solar_ano = np.array([
        conta_solar_mes * 12 * (1 + reajuste) ** (ano - 1)
        if ano > 0 else 0
        for ano in anos
    ])

    manutencao_ano = np.array([
        manutencao_b_ano if ano > 0 else 0
        for ano in anos
    ])

    acum_a = capex_a + np.cumsum(conta_ano)

    acum_a2 = capex_a_extensao + np.cumsum(conta_ano)

    acum_b = (
        capex_b
        + np.cumsum(conta_solar_ano + manutencao_ano)
    )

    # CÁLCULO DO PAYBACK
    def cruzamento(serie_a, serie_b):
        diferenca = serie_b - serie_a

        if diferenca[0] <= 0:
            return 0.0

        for i in range(1, len(anos)):
            if diferenca[i] <= 0:
                d0 = diferenca[i - 1]
                d1 = diferenca[i]

                if d1 == d0:
                    return float(anos[i])

                fracao = -d0 / (d1 - d0)

                return float(anos[i - 1] + fracao)

        return None

    payback_a = cruzamento(acum_a, acum_b)
    payback_a2 = cruzamento(acum_a2, acum_b)

    return {
        "tarifa_com_tributos": tarifa,
        "kwh_faturado_mes": kwh_faturado,

        "conta_mes": conta_mes,
        "conta_solar_mes": conta_solar_mes,

        "capex_a": capex_a,
        "capex_a_extensao": capex_a_extensao,

        "custo_paineis": custo_paineis,
        "capex_b_base": capex_b_base,
        "reserva_solar": reserva_solar,
        "capex_b": capex_b,

        "diferenca_investimento": diferenca_investimento,

        "manutencao_b_ano": manutencao_b_ano,
        "manutencao_b_mes": manutencao_b_mes,

        "custo_operacional_solar_mes": custo_operacional_solar_mes,
        "economia_mes": economia_mes,

        "anos": anos,
        "conta_ano": conta_ano,
        "conta_solar_ano": conta_solar_ano,
        "manutencao_ano": manutencao_ano,

        "acum_a": acum_a,
        "acum_a_extensao": acum_a2,
        "acum_b": acum_b,

        "tco_a": float(acum_a[-1]),
        "tco_a_extensao": float(acum_a2[-1]),
        "tco_b": float(acum_b[-1]),

        "diferenca_tco": float(acum_b[-1] - acum_a[-1]),

        "payback_a_anos": payback_a,
        "payback_a_extensao_anos": payback_a2
    }
    
# INDICADORES AMBIENTAIS
def ambiental(p, c):
    """
    Estima as emissões associadas ao consumo elétrico
    e o potencial de emissões evitadas.
    """

    kg_ano = (
        c["kwh_ano"]
        * p["fator_emissao_kg_kwh"]
    )

    return {
        "co2_rede_kg_ano": kg_ano,
        "co2_evitado_kg_ano": kg_ano,
        "co2_evitado_faixa_kg_ano": (
            c["kwh_ano"] * 0.0215,
            c["kwh_ano"] * 0.0385
        ),
    }


# SIMULAÇÃO OPERACIONAL
def simular_ano(
    p,
    wh_dia_fixo_sem_bomba,
    potencia_bomba_w=40,
    semente=42
):
    """
    Simulação diária de 365 dias.

    Considera:
    - Geração solar;
    - Armazenamento na bateria;
    - Variação da umidade do solo;
    - Acionamento automático da bomba;
    - Energia não atendida.

    Os dados são sintéticos e demonstrativos.
    Não representam medições reais.
    """

    rng = np.random.default_rng(semente)

    datas = pd.date_range(
        "2027-01-01",
        periods=365,
        freq="D"
    )

    cap_wh = (
        p["bateria_ah"]
        * p["tensao_bateria_v"]
    )

    soc = 0.8 * cap_wh

    umid = 55.0

    linhas = []

    for d in datas:

        hsp = HSP_MENSAL[d.month - 1]

        # Variação sintética das condições climáticas
        nuvem = rng.choice(
            [1.0, 0.6, 0.25],
            p=[0.55, 0.30, 0.15]
        )

        chuva = (
            rng.random()
            < (
                0.30
                if d.month in (12, 1, 2, 3)
                else 0.08
            )
        )

        if chuva:
            nuvem = min(nuvem, 0.3)

        # Energia gerada pelo painel
        gera = (
            p["painel_wp"]
            * hsp
            * nuvem
            * p["desempenho_global_pr"]
        )

        # Variação da umidade do solo
        umid = max(
            10.0,
            umid - 8.0
        )

        if chuva:
            umid = min(
                80.0,
                umid + rng.uniform(15, 35)
            )

        # Acionamento automático da bomba
        bomba_min = 0.0

        if umid < 35:
            bomba_min = min(
                60.0,
                (55 - umid) / 0.9
            )

            umid = min(
                60.0,
                umid + 0.9 * bomba_min
            )

        consumo_bomba = (
            potencia_bomba_w
            * bomba_min / 60
        )

        consumo_total = (
            wh_dia_fixo_sem_bomba
            + consumo_bomba
        )

        # Atualização do estado de carga
        soc = soc + gera - consumo_total

        soc = min(
            soc,
            cap_wh
        )

        # Limite mínimo de descarga
        faltou = 0.0

        piso = (
            cap_wh
            * (1 - p["dod_lifepo4"])
        )

        if soc < piso:
            faltou = piso - soc
            soc = piso

        linhas.append({
            "data": d,
            "hsp_dia": round(hsp * nuvem, 2),
            "geracao_wh": round(gera, 1),
            "consumo_wh": round(consumo_total, 1),
            "bomba_min": round(bomba_min, 1),
            "umidade_solo_pct": round(umid, 1),
            "soc_pct": round(
                100 * soc / cap_wh,
                1
            ),
            "energia_nao_atendida_wh": round(
                faltou,
                1
            ),
        })

    return pd.DataFrame(linhas)


# INDICADORES DO DASHBOARD
def indicadores(p, c, comp, amb, sim):
    """
    Consolida os indicadores utilizados no dashboard.
    """

    consumo_simulado = sim["consumo_wh"].sum()

    energia_nao_atendida = (
        sim["energia_nao_atendida_wh"].sum()
    )

    if consumo_simulado > 0:
        atendido = (
            1 - energia_nao_atendida / consumo_simulado
        )
    else:
        atendido = 0

    return {
        "consumo_kwh_mes": c["kwh_mes"],

        "economia_rs_mes": comp["economia_mes"],

        "pct_energia_renovavel": 100 * atendido,

        "co2_evitado_kg_ano": amb["co2_evitado_kg_ano"],

        "autonomia_dias": dimensionar_solar(
            c["wh_dia"],
            p
        )["autonomia_dias"],

        "dias_com_falta": int(
            (sim["energia_nao_atendida_wh"] > 0).sum()
        ),
    }


# EXECUÇÃO COMPLETA
def tudo(p=None, equip=None):
    """
    Executa todas as etapas do projeto e retorna
    os resultados organizados para o dashboard.
    """

    p = p if p is not None else carregar_premissas()

    equip = (
        equip
        if equip is not None
        else carregar_equipamentos()
    )

    # Consumo dos equipamentos
    tabela, c = consumo(equip)

    # Dimensionamento solar
    dim = dimensionar_solar(
        c["wh_dia"],
        p
    )

    # Comparação financeira
    comp = comparar(
        p,
        c
    )

    # Indicadores ambientais.
    amb = ambiental(
        p,
        c
    )

    # Consumo fixo sem a bomba
    mascara_sem_bomba = (
        ~tabela["equipamento"]
        .str.contains("Bomba", case=False)
    )

    fixo = tabela.loc[
        mascara_sem_bomba,
        "wh_dia"
    ].sum()

    # Potência da bomba
    mascara_bomba = (
        equip["equipamento"]
        .str.contains("Bomba", case=False)
    )

    if not mascara_bomba.any():
        raise ValueError(
            "Nenhuma bomba foi encontrada em equipamentos.csv."
        )

    pot_bomba = float(
        equip.loc[
            mascara_bomba,
            "potencia_w"
        ].iloc[0]
    )

    # Simulação anual
    sim = simular_ano(
        p,
        fixo,
        pot_bomba
    )

    # Indicadores consolidados
    ind = indicadores(
        p,
        c,
        comp,
        amb,
        sim
    )

    return {
        "p": p,
        "tabela": tabela,
        "c": c,
        "dim": dim,
        "comp": comp,
        "amb": amb,
        "sim": sim,
        "ind": ind,
    }


# EXECUÇÃO PELO TERMINAL
if __name__ == "__main__":

    resultado = tudo()

    print("\n--- CONSUMO DOS EQUIPAMENTOS ---")

    print(
        resultado["tabela"][
            ["equipamento", "wh_dia", "kwh_mes"]
        ].to_string(index=False)
    )

    print("\n--- CONSUMO TOTAL ---")

    print({
        chave: round(valor, 3)
        for chave, valor in resultado["c"].items()
    })

    print("\n--- DIMENSIONAMENTO SOLAR ---")

    print({
        chave: round(valor, 3)
        for chave, valor in resultado["dim"].items()
    })

    print("\n--- COMPARAÇÃO FINANCEIRA ---")

    comp = resultado["comp"]

    for chave, valor in comp.items():
        if isinstance(valor, np.ndarray):
            continue

        if isinstance(valor, (float, np.floating)):
            print(f"{chave}: {valor:.2f}")
        else:
            print(f"{chave}: {valor}")

    print("\n--- INDICADORES AMBIENTAIS ---")

    print(resultado["amb"])

    print("\n--- INDICADORES DO DASHBOARD ---")

    print({
        chave: round(valor, 2)
        for chave, valor in resultado["ind"].items()
    })

    print("\n--- SIMULAÇÃO ---")

    sim = resultado["sim"]

    print(
        "Média de acionamento da bomba:",
        round(sim["bomba_min"].mean(), 1),
        "minutos/dia"
    )

    print(
        "Consumo médio:",
        round(sim["consumo_wh"].mean(), 1),
        "Wh/dia"
    )

    print(
        "Energia não atendida:",
        round(sim["energia_nao_atendida_wh"].sum(), 1),
        "Wh/ano"
    )
