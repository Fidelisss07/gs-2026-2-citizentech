"""Gera as figuras estáticas a partir dos mesmos cálculos do dashboard."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from calculos import tudo, RAIZ

SAIDA = RAIZ / "figuras"
SAIDA.mkdir(exist_ok=True)
VERDE, AZUL, CINZA, LARANJA = "#2E7D32", "#1565C0", "#546E7A", "#EF6C00"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})


def diagrama():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis("off")

    def caixa(x, y, w, h, texto, cor, fs=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.15",
                                    fc=cor, ec="none"))
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", color="white",
                fontsize=fs, fontweight="bold", linespacing=1.4)

    def seta(x1, y1, x2, y2, rot="", dy=0.22):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=18,
                                     lw=2, color="#37474F", shrinkA=2, shrinkB=2))
        if rot:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + dy, rot, ha="center", fontsize=10, color="#37474F")

    ax.text(8, 8.6, "Ciclo Verde: diagrama de blocos da solução", ha="center", fontsize=18, fontweight="bold")

    # Linha 1: fonte de energia
    ax.text(0.4, 7.85, "1. Fonte de energia", fontsize=12, color=LARANJA, fontweight="bold")
    caixa(0.4, 6.4, 3.0, 1.2, "Painel solar\n2 x 150 Wp", LARANJA)
    caixa(4.4, 6.4, 3.0, 1.2, "Controlador\nMPPT 40 A", LARANJA)
    caixa(8.4, 6.4, 3.0, 1.2, "Bateria LiFePO4\n12,8 V / 100 Ah", LARANJA)
    seta(3.4, 7.0, 4.4, 7.0, "CC"); seta(7.4, 7.0, 8.4, 7.0, "CC")

    # Cargas
    ax.text(12.4, 7.85, "2. Equipamentos", fontsize=12, color=VERDE, fontweight="bold")
    caixa(12.4, 6.7, 3.2, 0.9, "Bomba 40 W", VERDE)
    caixa(12.4, 5.5, 3.2, 0.9, "2 refletores 20 W, 12 h", VERDE)
    caixa(12.4, 4.3, 3.2, 0.9, "ESP32 + sensor 1 W", VERDE)
    seta(11.4, 7.0, 12.4, 7.15); seta(11.4, 6.8, 12.4, 5.95); seta(11.4, 6.6, 12.4, 4.75)

    # Linha 2: sensores e automação
    ax.text(0.4, 4.9, "3. Sensores e automação", fontsize=12, color=AZUL, fontweight="bold")
    caixa(0.4, 3.3, 4.6, 1.3, "Sensores\numidade do solo, luminosidade,\ntensão e corrente da bateria", AZUL, 10.5)
    caixa(6.2, 3.3, 5.0, 1.3, "Lógica de automação\numidade < 35 %: liga a bomba (máx. 1 h/dia)\nanoitecer: liga os refletores", AZUL, 10.5)
    seta(5.0, 3.95, 6.2, 3.95, "leituras")
    seta(11.2, 4.4, 12.4, 5.7, "")
    ax.text(10.4, 4.85, "comandos (relés)", fontsize=10, color="#37474F")
    seta(9.9, 6.4, 9.9, 4.6, "tensão e corrente", dy=0.0)

    # Linha 3: processamento e dashboard
    ax.text(3.2, 2.2, "4. Processamento e indicadores", fontsize=12, color=CINZA, fontweight="bold")
    caixa(0.4, 0.5, 4.4, 1.3, "Processamento\nESP32 envia por Wi-Fi\nWh, SOC e minutos de bomba", CINZA, 10.5)
    caixa(5.8, 0.5, 4.0, 1.3, "Neighborhood Action\nDashboard (Python)", CINZA, 10.5)
    caixa(10.8, 0.5, 4.8, 1.3, "Indicadores\nkWh/mês, R$/mês, % renovável,\nCO2 evitado, autonomia", CINZA, 10.5)
    seta(2.6, 3.3, 2.6, 1.8)
    seta(4.8, 1.15, 5.8, 1.15); seta(9.8, 1.15, 10.8, 1.15)
    fig.savefig(SAIDA / "diagrama_blocos.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def graficos(r):
    t, comp, sim = r["tabela"], r["comp"], r["sim"]

    fig, ax = plt.subplots(figsize=(9, 5))
    nomes = ["Bomba", "ESP32 + sensor", "2 refletores LED"]
    cores = [AZUL, CINZA, LARANJA]
    ax.bar(nomes, t["wh_dia"], color=cores)
    for i, v in enumerate(t["wh_dia"]):
        ax.text(i, v + 5, f"{v:.0f} Wh", ha="center")
    ax.set_ylabel("Wh por dia")
    ax.set_title(f"Consumo diário: {r['c']['wh_dia']:.0f} Wh ({r['c']['kwh_mes']:.2f} kWh/mês)".replace(".", ","))
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(SAIDA / "consumo_equipamentos.png", dpi=150, bbox_inches="tight"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(comp["anos"], comp["acum_a"], color=CINZA, lw=3, label="A: rede nova (padrão de entrada + conta)")
    ax.plot(comp["anos"], comp["acum_a_extensao"], color=CINZA, lw=2, ls="--", label="A2: rede com ponto já existente")
    ax.plot(comp["anos"], comp["acum_b"], color=LARANJA, lw=3, label="B: painel solar + bateria")
    ax.set_xlabel("Anos"); ax.set_ylabel("Custo acumulado (R$)")
    ax.set_title("Custo acumulado em 10 anos (estimativa)")
    ax.legend(frameon=False); ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(SAIDA / "custo_acumulado.png", dpi=150, bbox_inches="tight"); plt.close(fig)

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    a1.plot(sim["data"], sim["soc_pct"], color=LARANJA)
    a1.axhline(20, color="red", ls=":", lw=1); a1.set_ylabel("Bateria (%)")
    a1.set_title("Simulação de um ano: carga da bateria e umidade do solo (dados sintéticos)")
    a2.plot(sim["data"], sim["umidade_solo_pct"], color=VERDE)
    a2.axhline(35, color="red", ls=":", lw=1); a2.set_ylabel("Umidade (%)")
    for a in (a1, a2):
        a.spines[["top", "right"]].set_visible(False)
    fig.savefig(SAIDA / "simulacao_anual.png", dpi=150, bbox_inches="tight"); plt.close(fig)

    ind = r["ind"]
    fig, ax = plt.subplots(figsize=(11, 3.6)); ax.axis("off")
    cards = [(f"{ind['consumo_kwh_mes']:.2f}".replace(".", ","), "kWh por mês"), (f"R$ {ind['economia_rs_mes']:.2f}".replace(".", ","), "economia estimada/mês"),
             (f"{ind['pct_energia_renovavel']:.1f} %".replace(".", ","), "renovável atendida"),
             (f"{ind['co2_evitado_kg_ano']:.1f} kg".replace(".", ","), "CO2 evitado/ano"), (f"{ind['autonomia_dias']:.1f} dias".replace(".", ","), "autonomia da bateria")]
    for i, (v, rot) in enumerate(cards):
        x = i * 0.2
        ax.add_patch(FancyBboxPatch((x + 0.005, 0.1), 0.19, 0.8, boxstyle="round,pad=0.01", fc="#E8F5E9", ec=VERDE, transform=ax.transAxes))
        ax.text(x + 0.1, 0.58, v, ha="center", fontsize=20, fontweight="bold", color=VERDE, transform=ax.transAxes)
        ax.text(x + 0.1, 0.30, rot, ha="center", fontsize=9, color="#37474F", transform=ax.transAxes, wrap=True)
    fig.savefig(SAIDA / "indicadores.png", dpi=150, bbox_inches="tight"); plt.close(fig)


if __name__ == "__main__":
    r = tudo()
    diagrama()
    graficos(r)
    print("figuras geradas em", SAIDA)
