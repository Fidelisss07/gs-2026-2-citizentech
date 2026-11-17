## Consumo energético
- Período de referência: 1 mês = 30 dias, 1 ano = 365 dias
- A energia de cada equipamento segue *E = (P * t)/1000*, com P em Watts, t em horas e E em kWh.
- O sistema inteiro opera em 12 V de corrente contínua, o que evita inversor e as perdas dele.

| Equipamento | Qtd | P (W) | t (h/dia) | Wh/dia = qtd * p * t | kWh/mês = (Wh/dia * 30)/1000  | kWh/ano = kWh/mês * 12 |
|---|---|---|---|---|---|---|
| Bomba de irrigação - 12V | 1 | 40 | 2 | 80 | 2,40 | 28,80 |
| ESP32 + sensor capacitivo | 1 | 1 | 24 | 24 | 0,72 | 8,64 |
| Refletor LED - 12V | 2 | 20 | 12 | 480 | 14,40 | 172,80 |
| Total | | | | 584 | 17,52 | 210,24 |


## Justificativa das premissas
- A bomba de 40W com 2h por dia é um limite superior: a automação só liga quando a umidade cai abaixo de 45%.
- O ESP32 com Wi-Fi consome entre 0,5 W e 1 W, e o sensor capacitivo consome cerca de 0,00004 Watts, então foi adotado 1W em 24h, que cobre os dois.
- Os refletores de 20W por 12h cobrem o período das 18h às 06h, eles respondem por 480 dos 584 Wh diários (82% do consumo), então a iluminação define o tamanho do sistema.
