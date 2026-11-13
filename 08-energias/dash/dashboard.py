"""
Rodar: streamlit run dash/dashboard.py
Os números vêm de calculos.py (premissas em data/premissas.json).
Os sliders da barra lateral permitem testar premissas e ver os indicadores mudarem.
"""
import copy
from pathlib import Path
import pandas as pd
import streamlit as st

from calculos import (
    tudo,
    carregar_premissas,
    carregar_equipamentos,
)

# CONFIGURAÇÃO
st.set_page_config(
    page_title="Ciclo Verde | Dashboard de energia",
    layout="wide"
)


def brl(valor):
    """Formata valores monetários no padrão brasileiro."""
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

# CARREGAMENTO DAS PREMISSAS
p0 = carregar_premissas()
eq0 = carregar_equipamentos()


# BARRA LATERAL — SIMULAÇÃO DE PREMISSAS

with st.sidebar:
    st.header("Premissas")
    st.caption("Valores iniciais: data/premissas.json")

    pot_led = st.slider(
        "Potência de cada refletor LED (W)",
        min_value=5,
        max_value=30,
        value=int(eq0.loc[2, "potencia_w"])
    )

    h_led = st.slider(
        "Horas de iluminação por noite",
        min_value=1,
        max_value=14,
        value=int(eq0.loc[2, "horas_dia"])
    )

    h_bomba = st.slider(
        "Horas de bomba por dia (máximo)",
        min_value=0.25,
        max_value=2.0,
        value=float(eq0.loc[0, "horas_dia"]),
        step=0.25
    )

    tarifa = st.number_input(
        "Tarifa Enel B3 sem tributos (R$/kWh)",
        value=float(p0["tarifa_enel_sem_tributos_kwh"]),
        format="%.5f"
    )

    reaj = st.slider(
        "Reajuste anual da tarifa",
        min_value=0.0,
        max_value=0.5,
        value=float(p0["reajuste_tarifa_aa"]),
        step=0.01,
        format="%.0f%%"
    )

    painel = st.select_slider(
        "Painel solar (Wp)",
        options=[100, 150, 200, 300, 450],
        value=p0["painel_wp"]
    )

    bateria = st.select_slider(
        "Bateria LiFePO4 12,8 V (Ah)",
        options=[30, 50, 100, 200],
        value=p0["bateria_ah"]
    )

    c_ah = st.number_input(
        "Preço da bateria por Ah (R$/Ah)",
        min_value=0.0,
        value=float(p0["custo_bateria_por_ah"]),
        step=1.0
    )


# ATUALIZAÇÃO DAS PREMISSAS
p = copy.deepcopy(p0)

p.update({
    "tarifa_enel_sem_tributos_kwh": tarifa,
    "reajuste_tarifa_aa": reaj,
    "painel_wp": painel,
    "bateria_ah": bateria,
    "custo_bateria": c_ah * bateria,
    "custo_painel": (
        p0["custo_painel"] * painel / p0["painel_wp"]
    )
})

eq = eq0.copy()

eq.loc[0, "horas_dia"] = h_bomba
eq.loc[2, "potencia_w"] = pot_led
eq.loc[2, "horas_dia"] = h_led

# EXECUÇÃO DOS CÁLCULOS
r = tudo(p, eq)

c = r["c"]
dim = r["dim"]
comp = r["comp"]
amb = r["amb"]
sim = r["sim"]
ind = r["ind"]
tabela = r["tabela"]

# TÍTULO E APRESENTAÇÃO
st.title(
    "Ciclo Verde: energia para a horta e o ponto de compostagem"
)

st.caption(
    "Mooca, São Paulo | Soluções em Energias Renováveis e Sustentáveis"
)

st.info(
    "Os valores apresentados são estimativas baseadas nas premissas "
    "do projeto. Utilize os controles laterais para testar diferentes "
    "cenários de consumo, dimensionamento e custos."
)


# INDICADORES GERAIS
st.subheader("Indicadores do projeto")

k = st.columns(5)

k[0].metric(
    "Consumo estimado",
    f"{ind['consumo_kwh_mes']:.2f} kWh/mês",
    f"{c['kwh_dia']:.3f} kWh/dia",
    delta_color="off"
)

k[1].metric(
    "Diferença operacional (A - B)",
    f"{brl(ind['economia_rs_mes'])}/mês",
    help=(
        "Conta mensal da rede elétrica menos a conta mensal solar "
        "e o equivalente mensal da manutenção solar. "
        "Valor negativo indica custo operacional maior na alternativa solar."
    ),
    delta_color="off"
)

k[2].metric(
    "Energia renovável atendida",
    f"{ind['pct_energia_renovavel']:.1f}%",
    f"{ind['dias_com_falta']} dias com falta na simulação",
    delta_color="off"
)

k[3].metric(
    "CO₂ evitado",
    f"{ind['co2_evitado_kg_ano']:.1f} kg/ano",
    help="Estimativa baseada no fator médio de emissão do SIN utilizado no projeto.",
    delta_color="off"
)

k[4].metric(
    "Autonomia da bateria",
    f"{ind['autonomia_dias']:.1f} dias",
    help="Capacidade útil da bateria considerando 80% de profundidade de descarga.",
    delta_color="off"
)


# CONSUMO ENERGÉTICO
st.divider()
st.subheader("Consumo estimado dos equipamentos")

st.markdown(
    "O consumo energético é estimado pela relação entre potência, "
    "tempo de utilização e quantidade de equipamentos."
)

st.latex(r"E = \frac{P \times t \times Q}{1000}")

t = tabela.copy()

t.columns = [
    "Equipamento",
    "Qtd",
    "Potência (W)",
    "Horas/dia",
    "Observação",
    "Wh/dia",
    "kWh/mês",
    "kWh/ano"
]

st.dataframe(
    t[
        [
            "Equipamento",
            "Qtd",
            "Potência (W)",
            "Horas/dia",
            "Wh/dia",
            "kWh/mês",
            "kWh/ano"
        ]
    ].round(2),
    hide_index=True,
    use_container_width=True
)

st.caption("Consumo diário estimado por equipamento.")

st.bar_chart(
    tabela.set_index("equipamento")["wh_dia"],
    horizontal=True
)


# COMPARAÇÃO FINANCEIRA
st.divider()
st.subheader("Comparação financeira das alternativas")

st.caption(
    "Comparação entre a conexão à rede elétrica convencional "
    "e a implantação de um sistema de energia solar."
)

a, b = st.columns(2)


# ALTERNATIVA A — REDE ELÉTRICA
with a:
    st.markdown("### A. Rede elétrica")

    st.metric(
        "Total de referência",
        brl(comp["total_referencia_a"])
    )

    st.metric(
        "Investimento de implementação",
        brl(comp["capex_a"])
    )

    st.metric(
        "Conta mensal estimada",
        brl(comp["conta_mes"])
    )

    st.metric(
        "Manutenção anual",
        brl(0)
    )

    st.caption(
        "O investimento considera instalação, equipamentos "
        "e documentação da alternativa elétrica."
    )


# ALTERNATIVA B — ENERGIA SOLAR
with b:
    st.markdown("### B. Energia solar")

    st.metric(
        "Total de referência",
        brl(comp["total_referencia_b"])
    )

    st.metric(
        "Investimento de implementação",
        brl(comp["capex_b"])
    )

    st.metric(
        "Conta mensal estimada",
        brl(comp["conta_solar_mes"])
    )

    st.metric(
        "Manutenção anual",
        brl(comp["manutencao_b_ano"])
    )

    st.caption(
        f"Equivalente mensal da manutenção: "
        f"{brl(comp['manutencao_b_mes'])}."
    )


st.caption(
    "Os totais de referência são valores consolidados utilizados "
    "para apresentação. A projeção financeira de 10 anos considera "
    "separadamente o investimento inicial, as contas mensais "
    "e os custos recorrentes de manutenção."
)

# PROJEÇÃO FINANCEIRA — 10 ANOS
st.divider()
st.subheader("Projeção de custos acumulados em 10 anos")

st.caption(
    "A projeção considera o investimento de implementação, "
    "as contas de energia e os custos de manutenção. "
    "Não considera a substituição da bateria, que pode ocorrer "
    "próximo ao fim do horizonte analisado."
)

pa = comp["payback_a_anos"]
pb = comp["payback_a_extensao_anos"]

m = st.columns(4)

m[0].metric(
    "Custo acumulado em 10 anos — A",
    brl(comp["tco_a"])
)

m[1].metric(
    "Custo acumulado em 10 anos — B",
    brl(comp["tco_b"])
)

m[2].metric(
    "Retorno de B contra A",
    (
        "Imediato"
        if pa == 0
        else (
            "Sem retorno em 10 anos"
            if pa is None
            else f"{pa:.1f} anos"
        )
    ),
    help=(
        "Comparação com a alternativa A: implantação de uma "
        "nova conexão à rede elétrica."
    )
)

m[3].metric(
    "Retorno de B contra A2",
    (
        "Sem retorno em 10 anos"
        if pb is None
        else f"{pb:.1f} anos"
    ),
    help=(
        "Comparação com a alternativa A2: já existe um ponto "
        "de energia próximo e só é necessário implantar o circuito interno."
    )
)


# SIMULAÇÃO OPERACIONAL
st.divider()
st.subheader("Operação simulada")

st.caption(
    "Dados sintéticos utilizados para demonstrar o funcionamento "
    "da automação e o comportamento do sistema ao longo de um ano."
)

s1, s2 = st.columns(2)

with s1:
    st.caption("Estado de carga da bateria (%) ao longo do ano")

    st.line_chart(
        sim.set_index("data")["soc_pct"]
    )

with s2:
    st.caption("Umidade do solo (%) — acionamento abaixo de 35%")

    st.line_chart(
        sim.set_index("data")["umidade_solo_pct"]
    )


st.write(
    f"Bomba: média simulada de "
    f"{sim['bomba_min'].mean():.1f} minutos por dia "
    f"(limite de projeto: {h_bomba * 60:.0f} minutos por dia). "
    f"Energia não atendida: "
    f"{sim['energia_nao_atendida_wh'].sum():.0f} Wh no ano."
)
