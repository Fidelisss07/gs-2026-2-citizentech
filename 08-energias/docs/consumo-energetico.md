# Consumo energético

- Período de referência: 1 mês = 30 dias; 1 ano = 365 dias.
- Sistema em corrente contínua de 12 V.
- Fórmula: E = (P × t × Q) / 1000.

| Equipamento | Qtd. | P (W) | h/dia | Wh/dia | kWh/mês | kWh/ano |
|---|---:|---:|---:|---:|---:|---:|
| Bomba de irrigação | 1 | 40 | 2 | 80 | 2,40 | 29,20 |
| ESP32 + sensor capacitivo | 1 | 1 | 24 | 24 | 0,72 | 8,76 |
| Refletores LED | 2 | 20 | 12 | 480 | 14,40 | 175,20 |
| **Total** | | | | **584** | **17,52** | **213,16** |

## Justificativa das premissas

- A bomba de 40 W, com até 2 horas de funcionamento por dia, representa um limite de consumo para o dimensionamento.
- O ESP32 com Wi-Fi e o sensor capacitivo possuem consumo estimado de 1 W para o conjunto.
- Os dois refletores de 20 W funcionam por até 12 horas por noite.
- A iluminação representa aproximadamente 82,2% do consumo diário.
- O acionamento automático da bomba ocorre quando a umidade do solo fica abaixo de 35%, conforme a lógica adotada na simulação.

O consumo mensal considera 30 dias. O consumo anual é calculado diretamente para 365 dias, por isso o valor anual não é obtido multiplicando o consumo mensal por 12.
