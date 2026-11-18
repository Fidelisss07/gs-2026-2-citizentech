# Comparação das alternativas e análise de sensibilidade
## Premissas gerais
- Local: Mooca, São Paulo.
- Período mensal: 30 dias.
- Período anual: 365 dias.
- Horizonte financeiro: 10 anos.
- Valores em reais de novembro de 2026.
- Reajuste tarifário: 0% no cenário-base.
- Valores financeiros são estimativas, sem cotação formal.


## 1. Consumo energético
A energia é calculada por:
E = (quantidade × potência × horas) / 1000

| Equipamento | Qtd. | Potência | Horas/dia | Wh/dia | kWh/mês |
|---|---:|---:|---:|---:|---:|
| Bomba de irrigação | 1 | 40 W | 2 | 80 | 2,40 |
| ESP32 + sensor | 1 | 1 W | 24 | 24 | 0,72 |
| Refletores LED | 2 | 20 W | 12 | 480 | 14,40 |
| **Total** | | | | **584** | **17,52** |

Consumo anual: 584 × 365 / 1000 = 213,16 kWh/ano.

A iluminação representa aproximadamente 82,2% do consumo diário.


## 2. Investimento inicial — Alternativa A: rede elétrica
| Item | Valor |
|---|---:|
| Instalação do padrão | R$ 2.500,00 |
| Equipamentos | R$ 1.000,00 |
| Documentação | R$ 1.200,00 |
| **CAPEX A** | **R$ 4.700,00** |

A conta mensal considera o custo de disponibilidade de 30 kWh.

Tarifa com tributos: 0,78938 / (1 - 0,18 - 0,06) = R$ 1,03866/kWh.

Conta mensal: 30 × 1,03866 = aproximadamente R$ 31,16.


## 3. Investimento inicial — Alternativa B: energia solar
| Item | Valor |
|---|---:|
| Dois painéis de 150 Wp | R$ 1.200,00 |
| Bateria LiFePO4 100 Ah | R$ 1.000,00 |
| Controlador MPPT | R$ 500,00 |
| Materiais e componentes BOS | R$ 600,00 |
| Mão de obra | R$ 1.000,00 |
| Documentação | R$ 400,00 |
| **CAPEX-base** | **R$ 4.700,00** |
| Adequações adicionais de infraestrutura | R$ 2.500,00 |
| **CAPEX B** | **R$ 7.200,00** |

A estimativa de R$ 2.500,00 contempla adequações adicionais de infraestrutura, fixação, proteção e instalação elétrica específica do sistema.

Esse valor é uma premissa orçamentária preliminar, sem cotação formal. Deve ser validado tecnicamente e não pode duplicar componentes já incluídos no BOS ou na mão de obra.

Diferença entre os investimentos iniciais: 7.200 - 4.700 = **R$2.500,00.**


## 4. Custos recorrentes
| Indicador | Rede elétrica | Solar |
|---|---:|---:|
| Conta mensal | R$ 31,16 | R$ 8,33 |
| Manutenção anual | R$ 0,00 | R$ 150,00 |
| Manutenção mensal equivalente | R$ 0,00 | R$ 12,50 |

A manutenção solar é uma provisão simplificada para limpeza e inspeção preventiva, com participação comunitária. Não inclui substituição de componentes ou assistência técnica profissional.


## 5. Comparação em dez anos
Fórmula: TCO = CAPEX + contas acumuladas + manutenção acumulada.

### Alternativa A — Rede elétrica
4.700 + (31,16 × 120)

TCO A = R$ 8.439,20.

### Alternativa B — Energia solar
7.200 + (8,33 × 120) + (150 × 10)

TCO B = R$ 9.699,60.

| Indicador | Rede elétrica | Solar |
|---|---:|---:|
| Investimento inicial | R$ 4.700,00 | R$ 7.200,00 |
| Contas em 10 anos | R$ 3.739,20 | R$ 999,60 |
| Manutenção em 10 anos | R$ 0,00 | R$ 1.500,00 |
| **TCO em 10 anos** | **R$ 8.439,20** | **R$ 9.699,60** |

Diferença de custo acumulado: 9.699,60 - 8.439,20 = **R$ 1.260,40.**

Com as premissas adotadas, a alternativa solar apresenta custo total estimado R$ 1.260,40 superior ao da nova ligação à rede elétrica no horizonte de dez anos.

Economia operacional mensal: 31,16 - 8,33 - 12,50 = R$ 10,33.

Apesar da economia operacional, ela não é suficiente para recuperar o investimento inicial adicional de R$ 2.500,00 em dez anos.


## 6. Cenário A2 — ponto de energia existente
Caso já exista um ponto de energia próximo, o investimento considerado é apenas a extensão do circuito interno, estimada em R$ 800,00.

TCO A2: 800 + (31,16 × 120) = R$ 4.539,20.
Nesse cenário, a extensão da rede apresenta menor custo acumulado que o sistema solar.

Portanto, a comparação econômica da energia solar com a rede deve distinguir uma nova ligação de uma simples extensão de circuito.


## 7. Dimensionamento solar
- Potência instalada: 300 Wp.
- Quantidade: 2 módulos de 150 Wp.
- HSP de projeto: 3,5.
- Desempenho global: 75%.
- Bateria: LiFePO4, 12,8 V e 100 Ah.
- Profundidade de descarga: 80%.
- Autonomia estimada: 1,75 dia.


## 8. Indicadores ambientais
Consumo anual: 213,16 kWh.

Fator médio de emissão: 0,0385 kg CO2/kWh.

Emissões da rede associadas à carga: 213,16 × 0,0385 = aproximadamente 8,21 kg CO2/ano.

Esse valor representa emissões operacionais potencialmente evitadas sob a hipótese de atendimento integral da carga pela energia solar. Não representa a pegada de carbono completa do sistema, pois fabricação e descarte dos componentes não estão incluídos.


## 9. Limitações
- Preços estimados, sem cotações formais.
- Adequações adicionais de R$ 2.500 sujeitas a validação técnica e orçamentária.
- Manutenção anual de R$ 150 sujeita a validação.
- Não foi incluída substituição da bateria no horizonte de dez anos.
- Reajuste tarifário de 0% no cenário-base.
- Geração e operação são estimativas e simulações, não medições reais.
- O cenário de nova ligação e o cenário de extensão de circuito possuem estruturas de investimento diferentes.
- O resultado financeiro depende das premissas de custos e não deve ser interpretado como orçamento definitivo.
