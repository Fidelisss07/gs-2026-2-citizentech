# 06 — Diário de Descarte da Casa | Ciclo Verde

Global Solution 2026.2 · Pensamento Computacional e Automação em Python · 1CCPR

## Integrantes

- Gustavo Fidelis de Souza e Silva — RM 574666
- Rafael Meirelles — RM 574897
- Anna Luisa Lima — RM 575081

## Introdução

O descarte inadequado de resíduos prejudica a limpeza e a qualidade de vida do bairro.
O público beneficiado são moradores que desejam acompanhar os resíduos de casa.
O programa registra tipo, destino e massa, classifica os descartes e resume os dados.
O objetivo é apoiar escolhas de destinação e o aproveitamento de orgânicos na compostagem.
O projeto se relaciona aos ODS 11 (cidades sustentáveis), 12 (consumo responsável) e 13 (ação climática).
As classificações são regras didáticas: a aceitação real deve ser confirmada em cada ponto de coleta.

## Execução

Requisito: Python 3.8 ou superior. Sem bibliotecas externas.

```powershell
python diario_descarte.py
```

O menu permite: 1 cadastrar, 2 consultar relatório, 3 listar e 4 sair.
Os dados ficam apenas na memória enquanto o programa estiver aberto; fechar apaga os registros.
Cada registro ocupa a mesma posição nas quatro listas de tipo, destino, massa e classificação.
O peso deve ser maior que zero e no máximo 1000 kg; vírgula e ponto são aceitos.
Letras, valores fora da faixa, NaN e infinito são rejeitados sem encerrar o programa.

## Regras do modelo

| Tipo | Destino classificado como correto no modelo |
|---|---|
| Orgânico | Compostagem |
| Reciclável | Coleta seletiva ou ecoponto |
| Óleo e eletrônico | Ecoponto ou ponto de entrega que aceite o material |
| Pilha/bateria | Ponto de entrega |
| Entulho e móvel | Ecoponto que aceite o material e volume |
| Rejeito | Coleta comum |

Rua/terreno é sempre incorreto. Essas regras não são uma lista oficial de aceitação de locais.
A massa enviada à compostagem não equivale à massa de adubo produzida; o programa não mede essa conversão.

## Indicadores e recomendação

O relatório calcula quantidade de registros, massa total, média, massa e percentual corretos,
orgânicos registrados e enviados à compostagem, massa destinada à rua e tipo predominante por massa.
Nível: ÓTIMO se percentual ≥80; REGULAR se 50≤percentual<80; PRECISA MELHORAR se <50.
O tipo mais descartado incorretamente e a massa na rua orientam a recomendação automática.
Empates de massa usam o primeiro tipo na ordem do menu.

## Demonstração com três registros

Cadastre, nesta ordem: orgânico/coleta comum/4 kg; entulho/rua/12 kg; reciclável/coleta seletiva/0,5 kg.
Depois escolha 3, 2 e 4 para listar, ver o relatório e encerrar.

Resultado da execução real:

```text
===== RELATORIO DA CASA =====
Descartes registrados ............ 3
Lixo total ....................... 16.5 kg
Media por descarte ............... 5.5 kg
Descartado certo ................. 0.5 kg (3%)
Organico que poderia virar adubo . 4.0 kg
Organico enviado a compostagem .. 0.0 kg
Jogado na rua/terreno ............ 12.0 kg
Tipo de lixo mais comum .......... Entulho
Nivel da casa .................... PRECISA MELHORAR
Descarte certo: [----------]

----- RECOMENDACAO -----
ATENCAO: 12.0 kg foram parar na rua ou em terreno.
Descarte na rua pode formar um ponto viciado. Consulte o ecoponto mais
proximo e confira quais materiais o local recebe.
O tipo que a casa mais descarta errado e: Entulho.
Dica: Entulho vai ao ecoponto, de graca. Na rua ele cria ponto viciado.

```

## Testes executados

- 48 combinacoes tipo x destino: OK
- Limites de classificacao 0 / 49.9 / 50 / 79.99 / 80 / 100: OK
- Entrada inteira: caracteres Unicode, letras, fora da faixa e numero excessivo: OK
- Peso: NaN, infinito, negativo, zero, acima do limite, letras e virgula: OK
- Calculo vazio protegido contra divisao por zero: OK
- Menu: relatorio e lista vazios; encerramento: OK
- Fluxo real de 3 registros, lista, relatorio e recomendacao: OK (16.5 kg, media 5.5 kg, 3% corretos)
- Cenario de descarte 100% correto: OK
- Fluxo real com entradas invalidas seguido de cadastro e relatorio: OK

As saídas reais dos fluxos de terminal foram conferidas durante os testes. O código usa funções,
listas, input/print, operadores, if/elif/else, for e while. `classificar` e `nivel` fazem classificação;
`calcular_indicadores` faz cálculo; as demais funções organizam entrada, cadastro e saída.

## Vídeo pitch final

O vídeo final está em `Ciclo_Verde_06_FINAL.mp4`, com duração de 1 minuto e 58 segundos,
gravação real do programa e narração gravada por Rafael. Os três integrantes estão
identificados na abertura. O vídeo apresenta o problema, três cadastros, a listagem,
os indicadores, a recomendação e a explicação da lógica.

**Link do vídeo:** https://youtu.be/L2nHecBaO0I

