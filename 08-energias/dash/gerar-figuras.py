"""Gera as figuras estáticas a partir dos mesmos cálculos do dashboard

As imagens são salvas na pasta fig/
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from calculos import tudo, RAIZ


# CONFIGURAÇÕES
SAIDA = RAIZ / "fig"
SAIDA.mkdir(parents=True, exist_ok=True)

VERDE = "#2E7D32"
AZUL = "#1565C0"
CINZA = "#546E7A"
LARANJA = "#EF6C00"
VERMELHO = "#C62828"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11
})


# FORMATAÇÃO MONETÁRIA
def brl(valor):
    """Formata valores no padrão monetário brasileiro."""

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


# DIAGRAMA DE BLOCOS
def diagrama():

    fig, ax = plt.subplots(figsize=(16, 9))

    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    def caixa(x, y, w, h, texto, cor, fs=10.5):

        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.04,rounding_size=0.15",
                fc=cor,
                ec="none"
            )
        )

        ax.text(
            x + w / 2,
            y + h / 2,
            texto,
            ha="center",
            va="center",
            color="white",
            fontsize=fs,
            fontweight="bold",
            linespacing=1.4
        )

    def seta(x1, y1, x2, y2, texto=None):

        ax.add_patch(
            FancyArrowPatch(
                (x1, y1),
                (x2, y2),
                arrowstyle="-|>",
                mutation_scale=18,
                lw=1.8,
                color="#37474F",
                shrinkA=2,
                shrinkB=2
            )
        )

        if texto:
            ax.text(
                (x1 + x2) / 2,
                (y1 + y2) / 2 + 0.18,
                texto,
                ha="center",
                fontsize=9,
                color="#37474F"
            )

    ax.text(
        8,
        8.55,
        "Ciclo Verde — Diagrama geral da solução",
        ha="center",
        fontsize=19,
        fontweight="bold"
    )

    # FONTE DE ENERGIA
    ax.text(
        0.5,
        7.75,
        "1. Geração e armazenamento de energia",
        fontsize=12,
        color=LARANJA,
        fontweight="bold"
    )

    caixa(
        0.5, 6.2, 3.0, 1.1,
        "Painel solar\n300 Wp",
        LARANJA
    )

    caixa(
        4.5, 6.2, 3.0, 1.1,
        "Controlador de carga\nMPPT",
        LARANJA
    )

    caixa(
        8.5, 6.2, 3.0, 1.1,
        "Bateria LiFePO4\n12,8 V / 100 Ah",
        LARANJA
    )

    seta(3.5, 6.75, 4.5, 6.75, "CC")
    seta(7.5, 6.75, 8.5, 6.75, "CC")

    # EQUIPAMENTOS
    ax.text(
        12.1,
        7.75,
        "2. Equipamentos",
        fontsize=12,
        color=VERDE,
        fontweight="bold"
    )

    caixa(
        12.1, 6.65, 3.4, 0.8,
        "Bomba de irrigação — 40 W",
        VERDE
    )

    caixa(
        12.1, 5.5, 3.4, 0.8,
        "2 refletores LED — 20 W cada",
        VERDE
    )

    caixa(
        12.1, 4.35, 3.4, 0.8,
        "ESP32 + sensor de umidade",
        VERDE
    )

    seta(11.5, 6.8, 12.1, 7.05)
    seta(11.5, 6.65, 12.1, 5.9)
    seta(11.5, 6.5, 12.1, 4.75)

    # SENSORES E AUTOMAÇÃO
    ax.text(
        0.5,
        4.9,
        "3. Monitoramento e automação",
        fontsize=12,
        color=AZUL,
        fontweight="bold"
    )

    caixa(
        0.5, 3.25, 4.4, 1.2,
        "Sensores\nUmidade do solo, luminosidade\ne monitoramento elétrico",
        AZUL
    )

    caixa(
        6.0, 3.25, 5.0, 1.2,
        "Lógica de automação\nUmidade abaixo de 35%: aciona a bomba\nAnoitecer: aciona a iluminação",
        AZUL
    )

    seta(4.9, 3.85, 6.0, 3.85, "Leituras")

    seta(11.0, 4.1, 12.1, 5.8, "Comandos")

    # PROCESSAMENTO E DASHBOARD
    ax.text(
        0.5,
        2.15,
        "4. Processamento e visualização dos dados",
        fontsize=12,
        color=CINZA,
        fontweight="bold"
    )

    caixa(
        0.5, 0.55, 4.2, 1.1,
        "Coleta de dados\nESP32 e sensores",
        CINZA
    )

    caixa(
        5.9, 0.55, 4.2, 1.1,
        "Processamento e análise\nCálculos e indicadores",
        CINZA
    )

    caixa(
        11.3, 0.55, 4.2, 1.1,
        "Dashboard Ciclo Verde\nVisualização dos resultados",
        CINZA
    )

    seta(2.6, 3.25, 2.6, 1.65)
    seta(4.7, 1.1, 5.9, 1.1)
    seta(10.1, 1.1, 11.3, 1.1)

    fig.savefig(
        SAIDA / "diagrama_blocos.png",
        dpi=180,
        bbox_inches="tight",
        facecolor="white"
    )

    plt.close(fig)


# CONSUMO DOS EQUIPAMENTOS
def grafico_consumo(r):

    tabela = r["tabela"]
    consumo_total = r["c"]

    fig, ax = plt.subplots(figsize=(10, 5.5))

    nomes = tabela["equipamento"].tolist()
    valores = tabela["wh_dia"].tolist()

    barras = ax.barh(
        nomes,
        valores,
        color=[AZUL, CINZA, LARANJA]
    )

    for barra, valor in zip(barras, valores):

        ax.text(
            valor + 2,
            barra.get_y() + barra.get_height() / 2,
            f"{valor:.1f} Wh",
            va="center",
            fontsize=10
        )

    ax.set_xlabel("Consumo diário (Wh)")
    ax.set_title(
        "Consumo energético diário por equipamento",
        fontsize=14,
        fontweight="bold"
    )

    ax.text(
        0.98,
        0.95,
        (
            f"Total: {consumo_total['wh_dia']:.1f} Wh/dia\n"
            f"{consumo_total['kwh_mes']:.2f} kWh/mês"
        ),
        transform=ax.transAxes,
        ha="right",
        va="top",
        bbox={
            "boxstyle": "round,pad=0.5",
            "facecolor": "#E8F5E9",
            "edgecolor": VERDE
        }
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    fig.savefig(
        SAIDA / "consumo_equipamentos.png",
        dpi=180,
        bbox_inches="tight"
    )

    plt.close(fig)


# CUSTO ACUMULADO EM 10 ANOS
def grafico_custos(r):

    comp = r["comp"]

    fig, ax = plt.subplots(figsize=(10, 5.5))

    ax.plot(
        comp["anos"],
        comp["acum_a"],
        color=CINZA,
        linewidth=2.8,
        label="A — Rede elétrica"
    )

    ax.plot(
        comp["anos"],
        comp["acum_a_extensao"],
        color=AZUL,
        linewidth=2.2,
        linestyle="--",
        label="A2 — Ponto de energia existente"
    )

    ax.plot(
        comp["anos"],
        comp["acum_b"],
        color=LARANJA,
        linewidth=2.8,
        label="B — Energia solar"
    )

    ax.set_title(
        "Projeção de custos acumulados em 10 anos",
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Período (anos)")
    ax.set_ylabel("Custo acumulado (R$)")

    ax.set_xticks(comp["anos"])

    ax.grid(
        axis="y",
        linestyle=":",
        alpha=0.5
    )

    ax.legend(
        frameon=False,
        loc="upper left"
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    fig.savefig(
        SAIDA / "custo_acumulado.png",
        dpi=180,
        bbox_inches="tight"
    )

    plt.close(fig)


# SIMULAÇÃO ANUAL
def grafico_simulacao(r):

    sim = r["sim"]

    fig, (ax1, ax2) = plt.subplots(
        2,
        1,
        figsize=(11, 7),
        sharex=True
    )

    # Estado de carga da bateria
    ax1.plot(
        sim["data"],
        sim["soc_pct"],
        color=LARANJA,
        linewidth=1.3
    )

    ax1.axhline(
        20,
        color=VERMELHO,
        linestyle=":",
        linewidth=1.5,
        label="Limite mínimo de carga"
    )

    ax1.set_ylabel("Carga da bateria (%)")

    ax1.set_title(
        "Simulação operacional anual — dados sintéticos",
        fontsize=14,
        fontweight="bold"
    )

    ax1.legend(frameon=False)

    # Umidade do solo
    ax2.plot(
        sim["data"],
        sim["umidade_solo_pct"],
        color=VERDE,
        linewidth=1.3
    )

    ax2.axhline(
        35,
        color=VERMELHO,
        linestyle=":",
        linewidth=1.5,
        label="Limite de acionamento da bomba"
    )

    ax2.set_ylabel("Umidade do solo (%)")
    ax2.set_xlabel("Data")

    ax2.legend(frameon=False)

    for eixo in (ax1, ax2):

        eixo.grid(
            axis="y",
            linestyle=":",
            alpha=0.4
        )

        eixo.spines["top"].set_visible(False)
        eixo.spines["right"].set_visible(False)

    fig.tight_layout()

    fig.savefig(
        SAIDA / "simulacao_anual.png",
        dpi=180,
        bbox_inches="tight"
    )

    plt.close(fig)


# INDICADORES DO PROJETO
def grafico_indicadores(r):

    ind = r["ind"]
    comp = r["comp"]

    fig, ax = plt.subplots(figsize=(12, 3.8))

    ax.axis("off")

    cards = [
        (
            f"{ind['consumo_kwh_mes']:.2f}".replace(".", ","),
            "kWh por mês"
        ),
        (
            brl(ind["economia_rs_mes"]),
            "Diferença operacional/mês"
        ),
        (
            f"{ind['pct_energia_renovavel']:.1f}%".replace(".", ","),
            "Energia atendida na simulação"
        ),
        (
            f"{ind['co2_evitado_kg_ano']:.1f} kg".replace(".", ","),
            "CO₂ potencialmente evitado/ano"
        ),
        (
            f"{ind['autonomia_dias']:.1f} dias".replace(".", ","),
            "Autonomia estimada"
        )
    ]

    largura = 0.18
    espacamento = 0.02

    for i, (valor, descricao) in enumerate(cards):

        x = i * (largura + espacamento)

        ax.add_patch(
            FancyBboxPatch(
                (x, 0.12),
                largura,
                0.76,
                boxstyle="round,pad=0.012",
                fc="#E8F5E9",
                ec=VERDE,
                transform=ax.transAxes
            )
        )

        ax.text(
            x + largura / 2,
            0.61,
            valor,
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            color=VERDE,
            transform=ax.transAxes
        )

        ax.text(
            x + largura / 2,
            0.34,
            descricao,
            ha="center",
            va="center",
            fontsize=8.5,
            color="#37474F",
            wrap=True,
            transform=ax.transAxes
        )

    ax.set_title(
        "Indicadores gerais do Ciclo Verde",
        fontsize=14,
        fontweight="bold",
        pad=12
    )

    fig.savefig(
        SAIDA / "indicadores.png",
        dpi=180,
        bbox_inches="tight",
        facecolor="white"
    )

    plt.close(fig)


# EXECUÇÃO
if __name__ == "__main__":

    print("Calculando os indicadores do Ciclo Verde...")

    resultado = tudo()

    print("Gerando diagrama...")
    diagrama()

    print("Gerando gráfico de consumo...")
    grafico_consumo(resultado)

    print("Gerando gráfico de custos...")
    grafico_custos(resultado)

    print("Gerando simulação anual...")
    grafico_simulacao(resultado)

    print("Gerando indicadores...")
    grafico_indicadores(resultado)

    print("\nImagens geradas com sucesso!")

    print(f"Local de saída: {SAIDA}")

    print("\nArquivos:")

    for arquivo in sorted(SAIDA.glob("*.png")):
        print(f"- {arquivo.name}")
