# Comparação das alternativas e sensibilidade
- Período de referência: 1 mês = 30 dias, 1 ano = 365 dias, horizonte de custos de 10 anos. 
- Valores em reais de novembro de 2026.

## Consumo energético
| Equipamento | Qtd | P (W) | t (h/dia) | Wh/dia = qtd * p * t | kWh/mês = (Wh/dia * 30)/1000  | kWh/ano = kWh/mês * 12 |
|---|---|---|---|---|---|---|
| Bomba de irrigação - 12V | 1 | 40 | 2 | 80 | 2,40 | 28,80 |
| ESP32 + sensor capacitivo | 1 | 1 | 24 | 24 | 0,72 | 8,64 |
| Refletor LED - 12V | 2 | 20 | 12 | 480 | 14,40 | 172,80 |
| Total | | | | 544 | 17,52 | 210,24 |


## Comparação
| Critério | A. Rede | B. Solar + bateria |
|---|---|---|
| Consumo | 17,52 kWh/mês (30 kWh faturados) | 17,52 kWh/mês, gerados no local |
| Instalação | R$4.731,16 | R$5.708,33 |
| Custo mensal | R$31,16 | R$8,33 |
| Custo em 10 anos | R$8.439,20 | R$6.699,60 |
| Viabilidade | Exige solicitação, vistoria e documentação da Enel; prazo da distribuidora | Instalação em um dia, sem burocracia com a Enel |
| Impacto ambiental | Rede com fator médio de 0,0385 kg CO₂/kWh | Sem emissão na operação |
| Vantagens | Sem limite de potência; sem bateria para trocar | Funciona em queda de rede; economia mensal; |
| Limitações | Conta mínima mesmo sem consumo; obra civil | Autonomia de 1,9 dia; depende de insolação; furto do painel exige fixação segura |

- Economia mensal estimada de B contra A: 31,16 − 8,33 = R$ 22,83.
- O investimento custa R$ 1.000,00 a mais na instalação (5.700,00 − 4.700,00). Esse valor se paga em 1.000 / (22,83 × 12) = 3,6 anos (3 anos e 6 meses).


## Sensibilidade
| Variação | Efeito |
|---|---|
| Refletores de 10W | Consumo 14,40 kWh/mês; painel mínimo 100Wp, bateria mínima 50Ah |
| Bateria a R$100,00 / R$ 1.300 | Instalação B de R$800,00 / R$ 1.300,00 |
| Padrão de entrada a R$ 1.800 / R$ 3.000 | Instalação A de R$ 2.600 / R$ 3.800 |
| Tarifa com reajuste de 5% ao ano | Custo de A em 10 anos sobe para R$9.403,14 |
| HSP de projeto 3,0 | Painel mínimo sobe para 135 Wp; o painel de 150 Wp ainda atende |
