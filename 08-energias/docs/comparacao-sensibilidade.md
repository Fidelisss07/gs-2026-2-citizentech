# Comparação das alternativas e análise de sensibilidade
## Premissas gerais
- Local: Mooca, São Paulo.
- Período mensal: 30 dias.
- Período anual: 365 dias.
- Horizonte financeiro: 10 anos.
- Valores em reais de novembro de 2026.
- Reajuste tarifário: 0% ao ano no cenário-base.
- Valores financeiros são estimativas preliminares, sem cotação formal.
- A alternativa solar é considerada um sistema isolado off-grid.

## Consumo energético
A energia consumida é calculada por: E = (quantidade × potência × horas de utilização) / 1000

| Equipamento | Quantidade | Potência | Horas/dia | Wh/dia | kWh/mês |
|---|---:|---:|---:|---:|---:|
| Bomba de irrigação | 1 | 40 W | 2 | 80 | 2,40 |
| ESP32 + sensor | 1 | 1 W | 24 | 24 | 0,72 |
| Refletores LED | 2 | 20 W | 12 | 480 | 14,40 |
| **Total** | | | | **584** | **17,52** |

Consumo anual: 584 × 365 / 1000 = **213,16 kWh/ano**.
A iluminação representa aproximadamente 82,2% do consumo diário.


## Alternativa A — nova ligação à rede elétrica
| Item | Valor |
|---|---:|
| Instalação do padrão | R$ 2.500,00 |
| Equipamentos | R$ 1.000,00 |
| Documentação | R$ 1.200,00 |
| **CAPEX A** | **R$ 4.700,00** |

A conta mensal considera o custo de disponibilidade de 30 kWh.

Tarifa sem tributos: R$ 0,78938/kWh.

Tributos adotados como premissa: ICMS de 18% e PIS/COFINS de 6%.

Tarifa estimada com tributos: 0,78938 / (1 - 0,18 - 0,06) = **R$ 1,03866/kWh**.

Conta mensal estimada: 30 × 1,03866 = **R$ 31,16/mês**.

### Manutenção e reposição
Foi adotada uma provisão de R$ 630,00 por ano para manutenção e reposição da infraestrutura elétrica interna.

Essa provisão é uma premissa do grupo, sujeita à validação técnica e orçamentária. Não representa uma cobrança da distribuidora nem um custo formalmente contratado.


## Alternativa B — sistema solar isolado
| Item | Valor |
|---|---:|
| Dois painéis de 150 Wp | R$ 1.200,00 |
| Bateria LiFePO4 de 100 Ah | R$ 1.000,00 |
| Controlador MPPT | R$ 500,00 |
| Materiais e componentes BOS | R$ 600,00 |
| Mão de obra | R$ 1.000,00 |
| Documentação | R$ 400,00 |
| **CAPEX-base** | **R$ 4.700,00** |
| Adequações adicionais de infraestrutura | R$ 3.500,00 |
| **CAPEX B** | **R$ 8.200,00** |

A reserva de R$ 3.500,00 contempla, como premissa preliminar, adequações específicas do local, como base e fixação, abrigo e proteção dos componentes e adequação da passagem de cabos.

O valor ainda precisa ser validado tecnicamente e por orçamento. Deve-se evitar duplicidade com materiais BOS e mão de obra já contabilizados.

Diferença entre os investimentos iniciais: 8.200 - 4.700 = **R$ 3.500,00**.

### Custos recorrentes
O sistema solar é considerado isolado off-grid, sem consumo faturado pela distribuidora. Por isso, a conta mensal de energia foi considerada R$ 0,00.

Foi adotada uma provisão de R$ 150,00 por ano para limpeza e inspeção preventiva, com participação comunitária.

## Comparação dos custos 

| Indicador | Rede elétrica | Solar off-grid |
|---|---:|---:|
| Conta mensal | R$ 31,16 | R$ 0,00 |
| Conta anual | R$ 373,92 | R$ 0,00 |
| Manutenção e reposição anual | R$ 630,00 | R$ 150,00 |
| Manutenção mensal equivalente | R$ 52,50 | R$ 12,50 |
| **Custo operacional anual** | **R$ 1.003,92** | **R$ 150,00** |

A diferença operacional anual estimada é: 1.003,92 - 150,00 = **R$ 853,92/ano**.


## Comparação do custo total em dez anos
Fórmula: TCO = CAPEX + contas acumuladas + manutenção acumulada.

### Alternativa A — rede elétrica
- Investimento inicial: R$ 4.700,00.
- Contas em dez anos: 31,16 × 120 = R$ 3.739,20.
- Manutenção e reposição em dez anos: 630 × 10 = R$ 6.300,00.
- TCO A: 4.700 + 3.739,20 + 6.300 = **R$ 14.739,20**.

### Alternativa B — energia solar
- Investimento inicial: R$ 8.200,00.
- Contas em dez anos: 0 × 120 = R$ 0,00.
- Manutenção em dez anos: 150 × 10 = R$ 1.500,00.
- TCO B: 8.200 + 0 + 1.500 = **R$ 9.700,00**.


### Resultado comparativo
| Indicador | Rede elétrica | Solar off-grid |
|---|---:|---:|
| Investimento inicial | R$ 4.700,00 | R$ 8.200,00 |
| Contas em dez anos | R$ 3.739,20 | R$ 0,00 |
| Manutenção em dez anos | R$ 6.300,00 | R$ 1.500,00 |
| **TCO em dez anos** | **R$ 14.739,20** | **R$ 9.700,00** |

Economia estimada do solar: 14.739,20 - 9.700,00 = **R$ 5.039,20**.

Portanto, apesar de exigir R$ 3.500,00 a mais no investimento inicial, a alternativa solar apresenta custo total estimado R$ 5.039,20 menor no horizonte de dez anos, considerando as provisões anuais adotadas.

### Payback estimado
O investimento adicional do solar é de R$ 3.500,00.
A economia operacional anual estimada é de R$ 853,92.

Payback simples:
3.500 / 853,92 = **aproximadamente 4,1 anos**.

O resultado é uma estimativa simplificada, sem considerar valor do dinheiro no tempo, inflação ou substituição de componentes.

## Cenário A2 — ponto de energia existente
Caso já exista um ponto de energia próximo, o investimento considerado é apenas a extensão do circuito interno, estimada em R$ 800,00.

| Indicador | Rede com extensão (A2) | Solar off-grid (B) |
|---|---:|---:|
| Investimento inicial | R$ 800,00 | R$ 8.200,00 |
| Contas em dez anos | R$ 3.739,20 | R$ 0,00 |
| Manutenção em dez anos | R$ 6.300,00 | R$ 1.500,00 |
| **TCO em dez anos** | **R$ 10.839,20** | **R$ 9.700,00** |

Diferença:
10.839,20 - 9.700,00 = **R$ 1.139,20 a favor do solar**.

Payback simples em relação ao cenário A2:

(8.200 - 800) / 853,92 = **aproximadamente 8,7 anos**.

A comparação econômica deve distinguir uma nova ligação à rede de uma simples extensão de circuito, pois os investimentos iniciais são diferentes.


## Dimensionamento solar
- Potência instalada: 300 Wp.
- Quantidade: dois módulos de 150 Wp.
- HSP de projeto: 3,5.
- Desempenho global: 75%.
- Bateria: LiFePO4, 12,8 V e 100 Ah.
- Profundidade de descarga: 80%.
- Energia nominal da bateria: 1.280 Wh.
- Energia útil estimada: 1.024 Wh.
- Autonomia estimada: 1,75 dia.

Geração estimada no cenário de projeto: 300 × 3,5 × 0,75 = **787,5 Wh/dia**.

A geração estimada supera o consumo diário de 584 Wh, mas não representa garantia de atendimento em qualquer condição climática.


## Indicadores ambientais
Consumo anual: 213,16 kWh.

Fator médio de emissão adotado: 0,0385 kg CO₂/kWh.

Emissões operacionais associadas à carga:

213,16 × 0,0385 = **aproximadamente 8,21 kg CO₂/ano**.

Esse valor representa emissões operacionais potencialmente evitadas sob a hipótese de atendimento integral da carga pela geração solar. Não representa a pegada de carbono completa do sistema, pois fabricação, transporte e descarte dos componentes não foram contabilizados.


## Limitações e análise de sensibilidade
- Os custos de instalação e adequação são estimativas sem cotação formal.
- A reserva solar de R$ 3.500,00 precisa ser validada tecnicamente.
- A provisão de R$ 630,00 anuais da rede é uma premissa do grupo, não um custo confirmado.
- A manutenção solar de R$ 150,00 anuais é uma provisão simplificada.
- A troca da bateria não foi incluída no horizonte de dez anos.
- O cenário-base considera reajuste tarifário de 0% ao ano.
- O resultado financeiro depende das premissas de custos e não deve ser interpretado como orçamento definitivo.
- A conta solar de R$ 0,00 depende de o sistema ser efetivamente isolado off-grid.
- Geração e operação são estimativas e simulações, não medições reais.
Uma alteração no custo de manutenção da rede, na tarifa de energia ou no custo de reposição da bateria pode modificar o resultado da comparação. Por isso, os valores devem ser tratados como cenário de estudo e não como garantia de economia futura.
