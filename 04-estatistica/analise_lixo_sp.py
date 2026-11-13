# GS 2026.2 - Estatística / Modelagem Linear para Aprendizado de Máquina
# Ciclo Verde - Turma 1CCPR
# Gustavo Fidelis de Souza e Silva (RM 574666)
# Rafael Meirelles (RM 574897)
# Ana (RM 575081)
#
# Análise estatística do lixo da cidade de São Paulo, com dados reais e oficiais.
# Base: base_lixo_sao_paulo.xlsx (na mesma pasta deste arquivo), com 3 abas:
#   - coleta_por_origem: toneladas de lixo coletadas por ano, segundo a origem
#     (Prefeitura de São Paulo; dados da AMLURB e da SP Regula; elaboração SMUL/Geoinfo)
#   - ecopontos: lista de ecopontos por subprefeitura
#     (Prefeitura de São Paulo, Secretaria Municipal das Subprefeituras)
#   - identificacao_e_fontes: integrantes, fontes completas e data da consulta
#
# Como rodar: python analise_lixo_sp.py
# Precisa de pandas, numpy e matplotlib (e do openpyxl, que o pandas usa para ler .xlsx).
# O programa mostra as tabelas e as medidas na tela e grava os gráficos na pasta "graficos".

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

PASTA = Path(__file__).resolve().parent
BASE = PASTA / "base_lixo_sao_paulo.xlsx"
PASTA_GRAFICOS = PASTA / "graficos"

VERDE = "#2E7D32"
VERDE_CLARO = "#81C784"
LARANJA = "#E65100"

pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 20)


# ===================================================================
# Funções de apoio
# ===================================================================

def titulo(texto):
    print("\n" + "=" * 80)
    print(texto)
    print("=" * 80)


def numero(valor, casas=0):
    """Formata no padrão brasileiro: 3549352 vira "3.549.352" e 21.34 vira "21,3"."""
    texto = f"{valor:,.{casas}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar(tabela, formatos):
    """Mostra uma tabela com os números formatados no padrão brasileiro."""
    copia = tabela.copy()
    for coluna, casas in formatos.items():
        copia[coluna] = copia[coluna].map(lambda v: numero(v, casas))
    print(copia.to_string())


# ===================================================================
# Exercício 01: a base de dados
# ===================================================================

def carregar_base():
    coleta = pd.read_excel(BASE, sheet_name="coleta_por_origem")
    ecopontos = pd.read_excel(BASE, sheet_name="ecopontos")
    identificacao = pd.read_excel(BASE, sheet_name="identificacao_e_fontes")
    return coleta, ecopontos, identificacao


def exercicio_01(coleta, ecopontos, identificacao):
    titulo("EXERCÍCIO 01 - A base de dados")
    for _, linha in identificacao.iterrows():
        if linha["campo"] == "Integrante":
            print("Integrante:", linha["valor"])
    print("\nAba coleta_por_origem (toneladas por ano):")
    for coluna in coleta.columns[1:]:
        com_dado = coleta[coleta[coluna].notna()]
        print(f"  {coluna:<28} {len(com_dado):>2} anos com dado "
              f"({com_dado['ano'].min()} a {com_dado['ano'].max()})")
    convencionais = ecopontos[ecopontos["tipo"] == "convencional"]
    print(f"\nAba ecopontos: {len(ecopontos)} ecopontos em {ecopontos['subprefeitura'].nunique()} subprefeituras "
          f"({len(convencionais)} convencionais e {len(ecopontos) - len(convencionais)} têxtil).")
    print("Fontes completas e observações: aba identificacao_e_fontes da base.")


def preparar_variaveis(coleta, ecopontos):
    """As duas variáveis do trabalho.

    Contínua: toneladas de lixo domiciliar coletadas por ano, de 2000 a 2025 (26 anos seguidos).
    Discreta: número de ecopontos convencionais em cada subprefeitura (31 subprefeituras).
    """
    serie_anual = coleta[coleta["ano"] >= 2000].set_index("ano")["residuo_domiciliar_t"]
    convencionais = ecopontos[ecopontos["tipo"] == "convencional"]
    por_subprefeitura = convencionais.groupby("subprefeitura").size().sort_values(ascending=False)
    por_subprefeitura.name = "ecopontos"
    return serie_anual, por_subprefeitura


# ===================================================================
# Exercício 02: tabelas de distribuição de frequências
# ===================================================================

def tabela_frequencia_discreta(serie):
    fi = serie.value_counts().sort_index()
    n = fi.sum()
    tabela = pd.DataFrame({"fi": fi})
    tabela["fri (%)"] = fi / n * 100
    tabela["Fi"] = fi.cumsum()
    tabela["Fri (%)"] = tabela["Fi"] / n * 100
    tabela.index.name = "ecopontos (x)"
    return tabela


def tabela_frequencia_continua(serie, arredondar_para=10_000):
    """Tabela com classes pela regra de Sturges: k = 1 + 3,322 x log10(n)."""
    n = len(serie)
    k = round(1 + 3.322 * math.log10(n))
    amplitude_total = serie.max() - serie.min()
    h = math.ceil(amplitude_total / k / arredondar_para) * arredondar_para
    inicio = math.floor(serie.min() / arredondar_para) * arredondar_para
    limites = [inicio + i * h for i in range(k + 1)]
    assert limites[-1] > serie.max()

    classes = pd.cut(serie, bins=limites, right=False)   # classes [a; b)
    fi = classes.value_counts().sort_index()
    tabela = pd.DataFrame({
        "classe (t)": [f"{numero(a)} |- {numero(b)}" for a, b in zip(limites[:-1], limites[1:])],
        "ponto médio (t)": [(a + b) / 2 for a, b in zip(limites[:-1], limites[1:])],
        "fi": fi.values,
    })
    tabela["fri (%)"] = tabela["fi"] / n * 100
    tabela["Fi"] = tabela["fi"].cumsum()
    tabela["Fri (%)"] = tabela["Fi"] / n * 100
    tabela.index = range(1, k + 1)
    tabela.index.name = "classe"
    return tabela, k, h, limites


def exercicio_02(serie_anual, por_subprefeitura):
    titulo("EXERCÍCIO 02 - Tabelas de distribuição de frequências")

    print("a) Variável quantitativa DISCRETA: número de ecopontos convencionais por subprefeitura")
    tabela_d = tabela_frequencia_discreta(por_subprefeitura)
    mostrar(tabela_d, {"fri (%)": 1, "Fri (%)": 1})
    print(f"Total: {tabela_d['fi'].sum()} subprefeituras.")

    print("\nb) Variável quantitativa CONTÍNUA: lixo domiciliar coletado por ano, 2000 a 2025 (toneladas)")
    tabela_c, k, h, limites = tabela_frequencia_continua(serie_anual)
    print(f"Regra de Sturges: n = {len(serie_anual)} anos, k = 1 + 3,322 x log10({len(serie_anual)}) "
          f"= {numero(1 + 3.322 * math.log10(len(serie_anual)), 2)} -> {k} classes; "
          f"amplitude de cada classe = {numero(h)} t")
    mostrar(tabela_c, {"ponto médio (t)": 0, "fri (%)": 1, "Fri (%)": 1})
    return tabela_d, tabela_c, h, limites


# ===================================================================
# Exercício 03: gráficos
# ===================================================================

def grafico_linha_domiciliar(serie_anual):
    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.axvspan(1999.5, 2006.9, color="#BDBDBD", alpha=0.35,
               label="Até nov/2006: a varrição era somada ao domiciliar")
    ax.plot(serie_anual.index, serie_anual.values / 1e6, color=VERDE, marker="o", linewidth=2,
            label="Lixo domiciliar coletado")
    ax.set_title("Lixo domiciliar coletado na cidade de São Paulo, 2000 a 2025", fontsize=13)
    ax.set_xlabel("Ano")
    ax.set_ylabel("Milhões de toneladas por ano")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: numero(v, 2)))
    ax.set_xticks(range(2000, 2026, 2))
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right")
    fig.text(0.01, 0.01,
             "Nota: segundo a fonte, até novembro de 2006 a varrição de ruas era contada junto com o lixo "
             "domiciliar (faixa cinza).\nFonte: Prefeitura de São Paulo, Coleta de resíduos segundo origem "
             "(AMLURB / SP Regula; SMUL/Geoinfo).", fontsize=8, color="#424242")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    caminho = PASTA_GRAFICOS / "grafico_1_linha_lixo_domiciliar.png"
    fig.savefig(caminho, dpi=150)
    return caminho


def grafico_barras_ecopontos(por_subprefeitura):
    ordem = por_subprefeitura.sort_values()   # a maior fica no topo do gráfico
    cores = [LARANJA if nome == "Mooca" else VERDE_CLARO for nome in ordem.index]
    fig, ax = plt.subplots(figsize=(10, 10))
    barras = ax.barh(ordem.index, ordem.values, color=cores, edgecolor="#424242", linewidth=0.5)
    ax.bar_label(barras, padding=3, fontsize=9)
    ax.set_title("Ecopontos convencionais por subprefeitura, cidade de São Paulo (nov/2026)", fontsize=13)
    ax.set_xlabel("Número de ecopontos")
    ax.set_ylabel("Subprefeitura")
    ax.grid(axis="x", alpha=0.3)
    ax.legend(handles=[Patch(color=LARANJA, label="Mooca (região do Ciclo Verde)"),
                       Patch(color=VERDE_CLARO, label="Outras subprefeituras")], loc="lower right")
    fig.text(0.01, 0.01,
             "Nota: a lista da Prefeitura não traz a subprefeitura de Parelheiros. O Ecoponto Têxtil (Mooca), "
             "que só recebe tecido, não entra na contagem.\nFonte: Prefeitura de São Paulo, Secretaria Municipal "
             "das Subprefeituras, lista de ecopontos (consulta em 13/11/2026).", fontsize=8, color="#424242")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    caminho = PASTA_GRAFICOS / "grafico_2_barras_ecopontos.png"
    fig.savefig(caminho, dpi=150)
    return caminho


def exercicio_03(serie_anual, por_subprefeitura):
    titulo("EXERCÍCIO 03 - Gráficos")
    PASTA_GRAFICOS.mkdir(exist_ok=True)
    print("Gráfico 1 (linha, variável contínua):", grafico_linha_domiciliar(serie_anual).name)
    print("Gráfico 2 (barras, variável discreta):", grafico_barras_ecopontos(por_subprefeitura).name)
    print(f"Gráficos gravados na pasta: {PASTA_GRAFICOS.name}")


# ===================================================================
# Exercício 04: análises univariadas
# ===================================================================

def modas_czuber(tabela_c, h, limites):
    """Moda para dados agrupados (fórmula de Czuber), usada quando nenhum valor se repete.

    Mo = limite inferior + h x d1 / (d1 + d2), com d1 = fi - f anterior e d2 = fi - f posterior.
    Se duas ou mais classes empatam na maior frequência, calcula a moda de cada uma.
    """
    fi = tabela_c["fi"].tolist()
    resultado = []
    for m, f in enumerate(fi):
        if f != max(fi):
            continue
        anterior = fi[m - 1] if m > 0 else 0
        posterior = fi[m + 1] if m + 1 < len(fi) else 0
        d1, d2 = f - anterior, f - posterior
        if d1 + d2 == 0:
            resultado.append((limites[m] + h / 2, m + 1))
        else:
            resultado.append((limites[m] + h * d1 / (d1 + d2), m + 1))
    return resultado


def analise_univariada(serie, casas, texto_moda):
    q1, q2, q3 = serie.quantile([0.25, 0.50, 0.75])
    media = serie.mean()
    desvio = serie.std()          # desvio padrão amostral (divide por n - 1)
    medidas = [
        ("Tendência central", "Média", numero(media, casas)),
        ("Tendência central", "Mediana", numero(serie.median(), casas)),
        ("Tendência central", "Moda", texto_moda),
        ("Dispersão", "Máximo", numero(serie.max(), casas)),
        ("Dispersão", "Mínimo", numero(serie.min(), casas)),
        ("Dispersão", "Amplitude", numero(serie.max() - serie.min(), casas)),
        ("Dispersão", "Variância (amostral, n - 1)", numero(serie.var(), casas)),
        ("Dispersão", "Desvio padrão (amostral)", numero(desvio, casas)),
        ("Dispersão", "Coeficiente de variação", numero(desvio / media * 100, 1) + "%"),
        ("Separatrizes", "Q1 (25%)", numero(q1, casas)),
        ("Separatrizes", "Q2 (50%, a mediana)", numero(q2, casas)),
        ("Separatrizes", "Q3 (75%)", numero(q3, casas)),
    ]
    return pd.DataFrame(medidas, columns=["grupo", "medida", "valor"])


def exercicio_04(serie_anual, por_subprefeitura, tabela_c, h, limites):
    titulo("EXERCÍCIO 04 - Análises univariadas (estatística descritiva)")

    print("Análise 1: lixo domiciliar coletado por ano, 2000 a 2025 (toneladas; n = 26)")
    modas = serie_anual.mode()
    if len(modas) == serie_anual.nunique():
        czuber = modas_czuber(tabela_c, h, limites)
        partes = " e ".join(f"{numero(mo)} (classe {classe})" for mo, classe in czuber)
        tipo = "bimodal" if len(czuber) == 2 else ("unimodal" if len(czuber) == 1 else "multimodal")
        texto_moda = (f"nenhum valor se repete; nos dados agrupados é {tipo}: "
                      f"moda de Czuber = {partes}")
    else:
        texto_moda = ", ".join(numero(v) for v in modas)
    print(analise_univariada(serie_anual, 0, texto_moda).to_string(index=False))
    print("Unidade: toneladas (a variância está em toneladas ao quadrado).")

    print("\nAnálise 2: ecopontos convencionais por subprefeitura (n = 31)")
    modas = por_subprefeitura.mode()
    contagem = (por_subprefeitura == modas.iloc[0]).sum()
    texto_moda = f"{', '.join(numero(v) for v in modas)} ({contagem} subprefeituras)"
    print(analise_univariada(por_subprefeitura, 2, texto_moda).to_string(index=False))
    mooca = por_subprefeitura["Mooca"]
    print(f"Mooca: {mooca} ecopontos convencionais, o maior valor; "
          f"{numero(mooca / por_subprefeitura.mean(), 1)} vezes a média das subprefeituras.")
    # Regra dos quartis (a mesma do boxplot): acima de Q3 + 1,5 x (Q3 - Q1) é valor fora do padrão.
    q1, q3 = por_subprefeitura.quantile([0.25, 0.75])
    limite = q3 + 1.5 * (q3 - q1)
    acima = por_subprefeitura[por_subprefeitura > limite]
    print(f"Valor fora do padrão: acima de Q3 + 1,5 x (Q3 - Q1) = {numero(limite, 1)}. "
          f"Passam desse limite: {', '.join(f'{nome} ({valor})' for nome, valor in acima.items())}.")


# ===================================================================
# Contexto para o relatório e diferencial
# ===================================================================

def contexto_coleta_seletiva(coleta):
    titulo("CONTEXTO - Coleta seletiva em relação ao lixo domiciliar (coluna calculada)")
    sel = coleta[coleta["coleta_seletiva_t"].notna()][["ano", "residuo_domiciliar_t", "coleta_seletiva_t"]].copy()
    sel["seletiva (% do domiciliar)"] = sel["coleta_seletiva_t"] / sel["residuo_domiciliar_t"] * 100
    mostrar(sel.set_index("ano"), {"residuo_domiciliar_t": 0, "coleta_seletiva_t": 0,
                                   "seletiva (% do domiciliar)": 2})


def diferencial_varricao_bueiros(coleta):
    titulo("DIFERENCIAL - Lixo da varrição x lixo tirado de bocas de lobo e bueiros (2013 a 2025)")
    dados = coleta[coleta["varricao_t"].notna() & coleta["bocas_de_lobo_e_bueiros_t"].notna()]
    x = dados["varricao_t"].astype(float).to_numpy()
    y = dados["bocas_de_lobo_e_bueiros_t"].astype(float).to_numpy()
    r = np.corrcoef(x, y)[0, 1]
    a, b = np.polyfit(x, y, 1)
    print(f"n = {len(dados)} anos | correlação de Pearson r = {numero(r, 2)} | r² = {numero(r * r, 2)} | "
          f"reta: bueiros = {numero(a, 3)} x varrição + {numero(b, 0)}")
    # Teste simples: o resultado depende de um ano só? Tira o ano mais longe da reta e calcula de novo.
    distancia = np.abs(y - (a * x + b))
    mais_longe = int(np.argmax(distancia))
    sem_ele = np.arange(len(x)) != mais_longe
    r_sem = np.corrcoef(x[sem_ele], y[sem_ele])[0, 1]
    print(f"Ano mais longe da reta: {dados['ano'].iloc[mais_longe]}. Sem ele, r = {numero(r_sem, 2)}.")
    print("Correlação não prova causa: os dois números podem mudar juntos por outros motivos.")

    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.scatter(x / 1000, y / 1000, color=VERDE, s=50, label="Um ano (2013 a 2025)")
    for ano, xi, yi in zip(dados["ano"], x, y):
        deslocamento = (4, 4) if ano % 2 == 0 else (4, -11)   # pares em cima, ímpares embaixo
        ax.annotate(str(ano), (xi / 1000, yi / 1000), textcoords="offset points", xytext=deslocamento, fontsize=8)
    xs = np.linspace(x.min(), x.max(), 50)
    ax.plot(xs / 1000, (a * xs + b) / 1000, color=LARANJA, linestyle="--",
            label=f"Reta de tendência (r = {numero(r, 2)})")
    ax.set_title("Varrição x bocas de lobo e bueiros, São Paulo, 2013 a 2025", fontsize=12)
    ax.set_xlabel("Lixo da varrição (mil toneladas por ano)")
    ax.set_ylabel("Lixo de bocas de lobo e bueiros (mil toneladas por ano)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    caminho = PASTA_GRAFICOS / "grafico_3_dispersao_varricao_bueiros.png"
    fig.savefig(caminho, dpi=150)
    print("Gráfico 3 (dispersão):", caminho.name)


# ===================================================================
# Programa principal
# ===================================================================

def principal():
    coleta, ecopontos, identificacao = carregar_base()
    exercicio_01(coleta, ecopontos, identificacao)
    serie_anual, por_subprefeitura = preparar_variaveis(coleta, ecopontos)
    tabela_d, tabela_c, h, limites = exercicio_02(serie_anual, por_subprefeitura)
    exercicio_03(serie_anual, por_subprefeitura)
    exercicio_04(serie_anual, por_subprefeitura, tabela_c, h, limites)
    contexto_coleta_seletiva(coleta)
    diferencial_varricao_bueiros(coleta)
    if plt.get_backend().lower() != "agg":   # abre as janelas só quando há tela
        plt.show()


if __name__ == "__main__":
    principal()
