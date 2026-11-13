## Consumo energético
A energia de cada equipamento segue *E = (P * t)/1000, com P em Watts, t em horas e E em kWh.
O sistema inteiro opera em 12 V de corrente contínua, o que evita inversor e as perdas dele.

| Equipamento | Qtd | P (W) | t (h/dia) | Wh/dia | kWh/mês | kWh/ano |
|---|---|---|---|---|---|---|
| Bomba de irrigação - 12V | 1 | 40 | 2 | 40 | 1,22 | 14,6 |
| ESP32 + sensor capacitivo | 1 | 1 | 24 | 24 | 0,73 | 8,8 |
| Refletor LED - 12V | 2 | 20 | 12 | 480 | 7,30 | 87,6 |
| Total | | | | 304 | 9,25 | 110,96 |


## Justificativa das premissas
- A bomba de 40W com 2h por dia é um limite superior: a automação só liga quando a umidade cai abaixo de 35%.
- O ESP32 com Wi-Fi consome entre 0,5 W e 1 W, e o sensor capacitivo consome cerca de 0,00004 Watts, então foi adotado 1W em 24h, que cobre os dois.
- Os refletores de 20W por 12h cobrem o período das 18h às 06h, quando não se tem mais luz natural.
