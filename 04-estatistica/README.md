# 04 — Estatística: o lixo de São Paulo com dados reais

**GS 2026.2 · Estatística / Modelagem Linear para Aprendizado de Máquina · Turma 1CCPR · Trio Ciclo Verde**

| Integrante | RM |
| --- | --- |
| Gustavo Fidelis de Souza e Silva (responsável pela 04) | 574666 |
| Rafael Meirelles | 574897 |
| Ana | 575081 |

Análise estatística com dados reais e oficiais da Prefeitura de São Paulo sobre o lixo da cidade, escrita para a Subprefeitura Mooca como cliente.

## Entrega no portal (3 arquivos, sem links)

| Arquivo | O que é |
| --- | --- |
| `base_lixo_sao_paulo.xlsx` | A base, com 3 abas: `coleta_por_origem` (toneladas por ano, 1980, 1991 e 2000 a 2025), `ecopontos` (132 ecopontos por subprefeitura) e `identificacao_e_fontes` (trio, fontes com endereço e data da consulta, observações) |
| `analise_lixo_sp.py` | O código dos exercícios 01 a 04: tabelas de frequência, gráficos e medidas |
| `relatorio_estatistico.pdf` | O relatório do exercício 05, com as tabelas, os gráficos e as medidas interpretados |

Outros arquivos desta pasta:
- `graficos/`: os 3 gráficos que o código gera.
- `relatorio.md`: o texto do relatório, de onde sai o PDF.

## Como rodar

```
pip install pandas numpy matplotlib openpyxl
python analise_lixo_sp.py
```

O programa mostra as tabelas e as medidas na tela, grava os gráficos em `graficos/` e abre as janelas dos gráficos.

## As duas variáveis

- **Discreta:** número de ecopontos convencionais em cada subprefeitura (31 subprefeituras). O Ecoponto Têxtil, que só recebe tecido, fica fora da contagem.
- **Contínua:** toneladas de lixo domiciliar coletadas por ano, de 2000 a 2025 (26 anos).

## Onde está cada exercício

| Exercício | No código | No relatório |
| --- | --- | --- |
| 01 · base de dados | `carregar_base`, `exercicio_01` | Seção 1 |
| 02 · tabelas de frequência (discreta e contínua) | `tabela_frequencia_discreta`, `tabela_frequencia_continua` (regra de Sturges) | Seção 2 |
| 03 · dois gráficos | `grafico_linha_domiciliar`, `grafico_barras_ecopontos` | Seção 3 |
| 04 · duas análises univariadas | `analise_univariada`, `modas_czuber` | Seção 4 |
| 05 · relatório | — | `relatorio_estatistico.pdf` |
| Extra · seletiva e varrição × bueiros | `contexto_coleta_seletiva`, `diferencial_varricao_bueiros` | Seções 5 e 6 |

## Fontes

- Prefeitura de São Paulo, tabela "Coleta de resíduos segundo origem" (AMLURB e SP Regula; elaboração SMUL/Geoinfo).
- Prefeitura de São Paulo, Secretaria Municipal das Subprefeituras, página dos ecopontos (lista consultada em 13/11/2026).

Os endereços completos e a data da consulta estão na aba `identificacao_e_fontes` da base e nas referências do relatório.

## Uso de IA

O Claude Code (Anthropic) ajudou a procurar as fontes, montar a base e escrever o rascunho do código e do relatório. As decisões foram do Fidelis e estão no próprio relatório (seção 9).
