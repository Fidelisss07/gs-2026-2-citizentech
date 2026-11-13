"""
Todos os números do dashboard vêm daqui. As premissas ficam em data/premissas.json
e os equipamentos em data/equipamentos.csv.
"""
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
DIAS_MES = 365 // 12
ANOS = 10

HSP_MENSAL = [5.2, 5.2, 4.7, 4.5, 3.9, 3.6, 3.8, 4.3, 4.2, 4.6, 5.0, 5.2]  # perfil sintético, média ≈ 4,5


def carregar_premissas():
    with open(RAIZ / "data" / "premissas.json", encoding="utf-8") as f:
        return json.load(f)


def carregar_equipamentos():
    return pd.read_csv(RAIZ / "data" / "equipamentos.csv")


def consumo(equip: pd.DataFrame):
    """E = (P x t) / 1000, somando quantidade x potência x horas."""
    df = equip.copy()
    df["wh_dia"] = df["quantidade"] * df["potencia_w"] * df["horas_dia"]
    df["kwh_mes"] = df["wh_dia"] * DIAS_MES / 1000
    df["kwh_ano"] = df["wh_dia"] * 365 / 1000
    total_wh = df["wh_dia"].sum()
    return df, {
        "wh_dia": total_wh,
        "kwh_dia": total_wh / 1000,
        "kwh_mes": total_wh * DIAS_MES / 1000,
        "kwh_ano": total_wh * 365 / 1000,
    }


def tarifa_com_tributos(p):
    return p["tarifa_enel_sem_tributos_kwh"] / (1 - p["icms"] - p["pis_cofins"])


def dimensionar_solar(wh_dia, p):
    pot_minima = wh_dia / (p["hsp_projeto"] * p["desempenho_global_pr"])
    cap_wh_min = wh_dia * p["autonomia_alvo_dias"] / p["dod_lifepo4"]
    ah_min = cap_wh_min / p["tensao_bateria_v"]
    cap_wh = p["bateria_ah"] * p["tensao_bateria_v"]
    autonomia = cap_wh * p["dod_lifepo4"] / wh_dia
    ger_media = p["painel_wp"] * p["hsp_media_anual"] * p["desempenho_global_pr"]
    ger_pior = p["painel_wp"] * p["hsp_projeto"] * p["desempenho_global_pr"]
    return {
        "painel_minimo_wp": pot_minima,
        "bateria_minima_ah": ah_min,
        "bateria_wh": cap_wh,
        "autonomia_dias": autonomia,
        "geracao_media_wh_dia": ger_media,
        "geracao_pior_mes_wh_dia": ger_pior,
        "folga_pior_mes": ger_pior / wh_dia - 1,
    }



def comparar(p, c):
    """Compara investimento e custos operacionais das alternativas."""

    tarifa = tarifa_com_tributos(p)

    kwh_faturado = max(
        c["kwh_mes"],
        p["custo_disponibilidade_kwh_mes"]
    )

    conta_mes = kwh_faturado * tarifa

    # Investimento inicial de implementação
    capex_a = (
        p["investimento_rede_instalacao"]
        + p["investimento_rede_equipamentos"]
        + p["investimento_rede_documentacao"]
    )

    # Cenário alternativo: já existe ponto de energia próximo
    capex_a_extensao = p["custo_circuito_interno"]

    capex_b = (
        p["custo_painel"]
        + p["custo_bateria"]
        + p["custo_controlador_mppt"]
        + p["custo_bos"]
        + p["custo_mao_obra_solar"]
        + p["documentacao_solar"]
    )

    # Contas e manutenção
    conta_solar_mes = p["conta_solar_mensal"]
    manutencao_solar_ano = p["manutencao_solar_ano"]

    # Horizonte de análise
    anos = np.arange(0, ANOS + 1)
    g = p["reajuste_tarifa_aa"]

    conta_ano = [
        conta_mes * 12 * (1 + g) ** (a - 1) if a > 0 else 0
        for a in anos
    ]

    operacao_solar_ano = [
        (conta_solar_mes * 12 * (1 + g) ** (a - 1)
         + manutencao_solar_ano) if a > 0 else 0
        for a in anos
    ]

    # Custos acumulados: implementação + operação
    acum_a = capex_a + np.cumsum(conta_ano)
    acum_a2 = capex_a_extensao + np.cumsum(conta_ano)
    acum_b = capex_b + np.cumsum(operacao_solar_ano)

    def interpolar_cruzamento(a, serie_a, serie_b):
        d0 = serie_b[a - 1] - serie_a[a - 1]
        d1 = serie_b[a] - serie_a[a]

        if d1 == d0:
            return float(a)

        return (a - 1) + (-d0) / (d1 - d0)

    def cruzamento(serie_a, serie_b):
        for a in anos:
            if serie_b[a] <= serie_a[a]:
                if a == 0:
                    return 0.0
                return interpolar_cruzamento(a, serie_a, serie_b)

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
        "capex_b": capex_b,

        "total_referencia_a": p["total_referencia_rede"],
        "total_referencia_b": p["total_referencia_solar"],

        "manutencao_b_ano": manutencao_solar_ano,
        "manutencao_b_mes": manutencao_solar_ano / 12,

        "om_b_mes": manutencao_solar_ano / 12,
        "economia_mes": (
            conta_mes - conta_solar_mes - manutencao_solar_ano / 12
        ),

        "anos": anos,
        "acum_a": acum_a,
        "acum_a_extensao": acum_a2,
        "acum_b": acum_b,

        "tco_a": float(acum_a[-1]),
        "tco_a_extensao": float(acum_a2[-1]),
        "tco_b": float(acum_b[-1]),

        "payback_a_anos": payback_a,
        "payback_a_extensao_anos": payback_a2,
    }
    
    def cruzamento(serie_a, serie_b):

        for ano in anos:

            if serie_b[ano] <= serie_a[ano]:

                if ano == 0:
                    return 0.0

                diferenca_anterior = (
                    serie_b[ano - 1] - serie_a[ano - 1]
                )

                diferenca_atual = (
                    serie_b[ano] - serie_a[ano]
                )

                if diferenca_atual == diferenca_anterior:
                    return float(ano)

                return (
                    ano - 1
                    + (-diferenca_anterior)
                    / (diferenca_atual - diferenca_anterior)
                )

        return None

    payback_a = cruzamento(acum_a, acum_b)
    payback_a2 = cruzamento(acum_a2, acum_b)

    # RESULTADOS
    return {
        "tarifa_com_tributos": tarifa,
        "kwh_faturado_mes": kwh_faturado,

        "conta_mes": conta_rede_mes,
        "conta_solar_mes": conta_solar_mes,

        "manutencao_solar_ano": manutencao_solar_ano,
        "manutencao_solar_mes": manutencao_solar_mes,

        "custo_recorrente_b_mes": custo_recorrente_b_mes,
        "economia_mes": economia_mes,

        "capex_a": capex_a,
        "capex_a_extensao": capex_a_extensao,
        "capex_b": capex_b,

        "anos": anos,
        "acum_a": acum_a,
        "acum_a_extensao": acum_a2,
        "acum_b": acum_b,

        "tco_a": float(acum_a[-1]),
        "tco_a_extensao": float(acum_a2[-1]),
        "tco_b": float(acum_b[-1]),

        "payback_a_anos": payback_a,
        "payback_a_extensao_anos": payback_a2
    }

    def cruzamento(serie_a, serie_b):
        for a in anos:
            if serie_b[a] <= serie_a[a]:
                return float(a) if a == 0 else _interpola(a, serie_a, serie_b)
        return None

    def _interpola(a, sa, sb):
        d0 = sb[a - 1] - sa[a - 1]
        d1 = sb[a] - sa[a]
        return (a - 1) + (-d0) / (d1 - d0) if d1 != d0 else float(a)

    payback_a = cruzamento(acum_a, acum_b)
    payback_a2 = cruzamento(acum_a2, acum_b)

    return {
        "tarifa_com_tributos": tarifa,
        "kwh_faturado_mes": kwh_faturado,
        "conta_mes": conta_mes,
        "capex_a": capex_a,
        "capex_a_extensao": capex_a_extensao,
        "capex_b": capex_b,
        "om_b_mes": p["om_solar_ano"] / 12,
        "economia_mes": conta_mes - p["om_solar_ano"] / 12,
        "anos": anos,
        "acum_a": acum_a,
        "acum_a_extensao": acum_a2,
        "acum_b": acum_b,
        "tco_a": float(acum_a[-1]),
        "tco_a_extensao": float(acum_a2[-1]),
        "tco_b": float(acum_b[-1]),
        "payback_a_anos": payback_a,
        "payback_a_extensao_anos": payback_a2,
    }


def ambiental(p, c):
    kg_ano = c["kwh_ano"] * p["fator_emissao_kg_kwh"]
    return {
        "co2_rede_kg_ano": kg_ano,
        "co2_evitado_kg_ano": kg_ano,
        "co2_evitado_faixa_kg_ano": (c["kwh_ano"] * 0.0215, c["kwh_ano"] * 0.0385),
    }


def simular_ano(p, wh_dia_fixo_sem_bomba, potencia_bomba_w=40, semente=42):
    """Simulação diária de 365 dias: geração, bateria, umidade do solo e bomba.

    Dados sintéticos para demonstrar a lógica de automação; não são medições.
    """
    rng = np.random.default_rng(semente)
    datas = pd.date_range("2027-01-01", periods=365, freq="D")
    cap_wh = p["bateria_ah"] * p["tensao_bateria_v"]
    soc = 0.8 * cap_wh
    umid = 55.0
    linhas = []
    for d in datas:
        hsp = HSP_MENSAL[d.month - 1]
        nuvem = rng.choice([1.0, 0.6, 0.25], p=[0.55, 0.30, 0.15])
        chuva = rng.random() < (0.30 if d.month in (12, 1, 2, 3) else 0.08)
        if chuva:
            nuvem = min(nuvem, 0.3)
        gera = p["painel_wp"] * hsp * nuvem * p["desempenho_global_pr"]
        umid = max(10.0, umid - 8.0)
        if chuva:
            umid = min(80.0, umid + rng.uniform(15, 35))
        bomba_min = 0.0
        if umid < 35:
            bomba_min = min(60.0, (55 - umid) / 0.9)
            umid = min(60.0, umid + 0.9 * bomba_min)
        consumo_bomba = potencia_bomba_w * bomba_min / 60
        consumo = wh_dia_fixo_sem_bomba + consumo_bomba
        soc = soc + gera - consumo
        soc = min(soc, cap_wh)
        faltou = 0.0
        piso = cap_wh * (1 - p["dod_lifepo4"])
        if soc < piso:
            faltou = piso - soc
            soc = piso
        linhas.append({
            "data": d, "hsp_dia": round(hsp * nuvem, 2), "geracao_wh": round(gera, 1),
            "consumo_wh": round(consumo, 1), "bomba_min": round(bomba_min, 1),
            "umidade_solo_pct": round(umid, 1), "soc_pct": round(100 * soc / cap_wh, 1),
            "energia_nao_atendida_wh": round(faltou, 1),
        })
    return pd.DataFrame(linhas)


def indicadores(p, c, comp, amb, sim):
    atendido = 1 - sim["energia_nao_atendida_wh"].sum() / sim["consumo_wh"].sum()
    return {
        "consumo_kwh_mes": c["kwh_mes"],
        "economia_rs_mes": comp["economia_mes"],
        "pct_energia_renovavel": 100 * atendido,
        "co2_evitado_kg_ano": amb["co2_evitado_kg_ano"],
        "autonomia_dias": dimensionar_solar(c["wh_dia"], p)["autonomia_dias"],
        "dias_com_falta": int((sim["energia_nao_atendida_wh"] > 0).sum()),
    }


def tudo(p=None, equip=None):
    p = p or carregar_premissas()
    equip = equip if equip is not None else carregar_equipamentos()
    tabela, c = consumo(equip)
    dim = dimensionar_solar(c["wh_dia"], p)
    comp = comparar(p, c)
    amb = ambiental(p, c)
    fixo = tabela.loc[~tabela["equipamento"].str.contains("Bomba"), "wh_dia"].sum()
    pot_bomba = float(equip.loc[equip["equipamento"].str.contains("Bomba"), "potencia_w"].iloc[0])
    sim = simular_ano(p, fixo, pot_bomba)
    ind = indicadores(p, c, comp, amb, sim)
    return {"p": p, "tabela": tabela, "c": c, "dim": dim, "comp": comp, "amb": amb, "sim": sim, "ind": ind}


if __name__ == "__main__":
    r = tudo()
    print(r["tabela"][["equipamento", "wh_dia", "kwh_mes"]])
    print({k: round(v, 3) for k, v in r["c"].items()})
    print({k: round(v, 3) for k, v in r["dim"].items()})
    comp = {k: (round(v, 2) if isinstance(v, float) else v) for k, v in r["comp"].items() if not isinstance(v, np.ndarray)}
    print(comp)
    print(r["amb"])
    print({k: round(v, 2) for k, v in r["ind"].items()})
    print("bomba média min/dia:", r["sim"]["bomba_min"].mean().round(1), "consumo médio Wh/dia:", r["sim"]["consumo_wh"].mean().round(1))
