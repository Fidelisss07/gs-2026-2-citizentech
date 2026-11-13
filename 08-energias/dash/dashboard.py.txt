Rodar: streamlit run dash/dashboard.py
Os números vêm de calculos.py (premissas em data/premissas.json).
Os sliders da barra lateral permitem testar premissas e ver os indicadores mudarem.
"""
import copy
from pathlib import Path
import pandas as pd
import streamlit as st

from calculos import tudo, carregar_premissas, carregar_equipamentos, RAIZ

st.set_page_config(page_title="Ciclo Verde | Dashboard de energia", layout="wide")

p0 = carregar_premissas()
eq0 = carregar_equipamentos()

with st.sidebar:
    st.header("Premissas")
    st.caption("Valores iniciais: data/premissas.json")
    pot_led = st.slider("Potência de cada refletor LED (W)", 5, 30, int(eq0.loc[2, "potencia_w"]))
    h_led = st.slider("Horas de luz por noite", 1, 14, int(eq0.loc[2, "horas_dia"]))
    h_bomba = st.slider("Horas de bomba por dia (máximo)", 0.25, 2.0, float(eq0.loc[0, "horas_dia"]), 0.25)
    tarifa = st.number_input("Tarifa Enel B3 sem tributos (R$/kWh)", value=p0["tarifa_enel_sem_tributos_kwh"], format="%.5f")
    reaj = st.slider("Reajuste anual da tarifa", 0.0, 0.5, p0["reajuste_tarifa_aa"], 0.01)
    painel = st.select_slider("Painel solar (Wp)", [100, 150, 200, 300, 450], p0["painel_wp"])
    bateria = st.select_slider("Bateria LiFePO4 12,8 V (Ah)", [30, 50, 100, 200], p0["bateria_ah"])
    c_ah = st.number_input("Preço da bateria por Ah (R$/Ah)", value=float(p0["custo_bateria_por_ah"]), step=1.0)
    c_pad = st.number_input("Padrão de entrada novo (R$)", value=float(p0["custo_padrao_entrada"]), step=100.0)

p = copy.deepcopy(p0)
p.update({"tarifa_enel_sem_tributos_kwh": tarifa, "reajuste_tarifa_aa": reaj, "painel_wp": painel,
          "bateria_ah": bateria, "custo_bateria": c_ah * bateria, "custo_padrao_entrada": c_pad,
          "custo_painel": p0["custo_painel"] * painel / p0["painel_wp"]})
eq = eq0.copy()
eq.loc[0, "horas_dia"] = h_bomba
eq.loc[2, "potencia_w"] = pot_led
eq.loc[2, "horas_dia"] = h_led

r = tudo(p, eq)
c, dim, comp, amb, sim, ind, tabela = r["c"], r["dim"], r["comp"], r["amb"], r["sim"], r["ind"], r["tabela"]

st.title("Ciclo Verde: energia para a horta e o ponto de compostagem (Mooca, São Paulo)")
st.caption("Contribuição de Soluções em Energias Renováveis e Sustentáveis. "
           "Todos os valores são estimativas que dependem das premissas ao lado, sem garantia de resultado.")

k = st.columns(5)
k[0].metric("Consumo", f"{ind['consumo_kwh_mes']:.2f} kWh/mês", f"{c['kwh_dia']:.3f} kWh/dia", delta_color="off")
k[1].metric("Economia estimada (B vs A)", f"R$ {ind['economia_rs_mes']:.2f}/mês", help="Conta da rede (mínimo faturável) menos manutenção do solar")
k[2].metric("Energia renovável atendida", f"{ind['pct_energia_renovavel']:.1f} %", f"{ind['dias_com_falta']} dias com falta na simulação", delta_color="off")
k[3].metric("CO₂ evitado", f"{ind['co2_evitado_kg_ano']:.1f} kg/ano", help="Consumo anual x fator médio do SIN (MCTI, 2023)")
k[4].metric("Autonomia da bateria", f"{ind['autonomia_dias']:.1f} dias", help="Capacidade útil (80 %) dividida pelo consumo diário")

st.subheader("1. Consumo estimado, E = (P × t) / 1000")
t = tabela.copy()
t.columns = ["Equipamento", "Qtd", "Potência (W)", "Horas/dia", "Observação", "Wh/dia", "kWh/mês", "kWh/ano"]
st.dataframe(t[["Equipamento", "Qtd", "Potência (W)", "Horas/dia", "Wh/dia", "kWh/mês", "kWh/ano"]].round(2), hide_index=True, width="stretch")
st.bar_chart(tabela.set_index("equipamento")["wh_dia"], horizontal=True)

st.subheader("2. Alternativa A (rede da Enel) contra alternativa B (painel solar e bateria)")
a, b = st.columns(2)
with a:
    st.markdown("**A. Rede elétrica**")
    st.write(f"Instalação: R$ {comp['capex_a']:,.0f} (padrão de entrada + circuito até a horta)")
    st.write(f"Classe tarifária B3 (demais classes). Faturado: {comp['kwh_faturado_mes']:.0f} kWh/mês (mínimo monofásico; o consumo real é {c['kwh_mes']:.1f} kWh)")
    st.write(f"Tarifa com tributos: R$ {comp['tarifa_com_tributos']:.3f}/kWh; conta ≈ R$ {comp['conta_mes']:.2f}/mês, mais a taxa de iluminação pública")
with b:
    st.markdown("**B. Solar + bateria**")
    st.write(f"Instalação: R$ {comp['capex_b']:,.0f} (painel {painel} Wp, MPPT, bateria {bateria} Ah, material e mão de obra)")
    st.write(f"Mínimo recomendado: painel {dim['painel_minimo_wp']:.0f} Wp e bateria {dim['bateria_minima_ah']:.0f} Ah; adotado {painel} Wp e {bateria} Ah")
    st.write(f"Geração no pior mês: {dim['geracao_pior_mes_wh_dia']:.0f} Wh/dia contra consumo de {c['wh_dia']:.0f} Wh/dia; manutenção ≈ R$ {comp['om_b_mes']:.2f}/mês")

df = pd.DataFrame({"Ano": comp["anos"], "A: rede nova": comp["acum_a"], "A2: ponto já existente": comp["acum_a_extensao"],
                   "B: solar + bateria": comp["acum_b"]}).set_index("Ano")
st.line_chart(df)
st.caption("Custo acumulado em 10 anos (instalação + operação). Sem a troca da bateria, que pode ocorrer perto do fim desse período.")
pa, pb = comp["payback_a_anos"], comp["payback_a_extensao_anos"]
m = st.columns(4)
m[0].metric("Custo em 10 anos, A", f"R$ {comp['tco_a']:,.0f}")
m[1].metric("Custo em 10 anos, B", f"R$ {comp['tco_b']:,.0f}")
m[2].metric("Retorno de B contra A", "imediato" if pa == 0 else ("sem retorno em 10 anos" if pa is None else f"{pa:.1f} anos"),
            help="A: rede nova (padrão de entrada + circuito + conta mínima).")
m[3].metric("Retorno de B contra A2", "sem retorno em 10 anos" if pb is None else f"{pb:.1f} anos",
            help="A2: já existe ponto de energia próximo e só falta o circuito.")

st.subheader("3. Operação simulada (dados sintéticos para demonstrar a automação)")
s1, s2 = st.columns(2)
s1.caption("Carga da bateria (%) ao longo de um ano")
s1.line_chart(sim.set_index("data")["soc_pct"])
s2.caption("Umidade do solo (%); a bomba liga abaixo de 35 %")
s2.line_chart(sim.set_index("data")["umidade_solo_pct"])
st.write(f"Bomba: média simulada de {sim['bomba_min'].mean():.1f} min/dia (limite de projeto: {h_bomba*60:.0f} min/dia). "
         f"Energia não atendida: {sim['energia_nao_atendida_wh'].sum():.0f} Wh no ano.")

st.subheader("4. Diagrama da solução")
img = RAIZ / "figuras" / "diagrama_blocos.png"
if img.exists():
    st.image(str(img))

st.subheader("5. Benefícios para a comunidade e limitações")
st.write("A horta ganha irrigação automática e luz noturna sem depender de ligação à rede, o que dispensa documentos de posse e obra civil. "
         "O voluntariado passa a regar com dados de umidade em vez de rotina fixa, e o painel serve de material didático.")
st.write(f"Limitações: o ganho de CO₂ é pequeno ({amb['co2_evitado_kg_ano']:.1f} kg/ano) porque a rede brasileira já é majoritariamente renovável, "
         "e a fabricação do painel e da bateria não entrou no cálculo. Preços de painel, bateria e padrão de entrada são estimativas de mercado "
         "que precisam de cotação. A irradiação solar é um perfil estimado a conferir no SunData/CRESESB com as coordenadas da horta.")
