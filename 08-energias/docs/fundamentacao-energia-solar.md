# Alternativa B: energia solar fotovoltaica
Este texto apresenta a fundamentação da alternativa de geração solar fotovoltaica com armazenamento em bateria. Os números de consumo vêm de `docs/consumo-energetico.md`. Os custos são premissas preliminares do grupo.


## Dimensionamento solar
Parâmetros adotados:
- HSP de projeto: 3,5 kWh/m²·dia.
- Desempenho global do sistema: 0,75.
- Bateria LiFePO4 com profundidade de descarga de 80%.
- Autonomia-alvo: 1,5 dia.

Potência mínima do painel: P = 584 / (3,5 × 0,75) = **222,5 Wp**.

Foram adotados dois módulos de 150 Wp, totalizando 300 Wp.

Geração estimada no cenário de projeto: 300 × 3,5 × 0,75 = **787,5 Wh/dia**.

Capacidade mínima da bateria: 584 × 1,5 / 0,8 = **1.095 Wh**, ou aproximadamente 85,5 Ah em 12,8 V.

Foi adotada uma bateria LiFePO4 de 12,8 V e 100 Ah, com energia nominal de 1.280 Wh. Considerando profundidade de descarga de 80%, a energia utilizável é de 1.024 Wh.

Autonomia estimada: 1.024 / 584 = **1,75 dia**.

O controlador adotado é MPPT de 40 A, sujeito à confirmação de compatibilidade elétrica com os módulos, a bateria e a configuração final do sistema.


## Benefícios da energia solar
A energia solar permite atender à demanda estimada de 17,52 kWh por mês para uma bomba, um sensor e duas luminárias, sem depender de uma ligação convencional à rede elétrica.

Com bateria, o sistema pode armazenar energia para utilização em períodos sem geração solar. Isso permite maior autonomia operacional e reduz a dependência de fornecimento externo.

A automação da irrigação permite acionar a bomba quando o sensor identifica umidade do solo abaixo do limite definido. As luminárias possibilitam o uso da horta no período noturno.

A alternativa também tem valor educativo, pois permite demonstrar geração renovável, armazenamento de energia, monitoramento e uso eficiente de recursos.


## Justificativa da escolha da energia solar
O sistema solar foi escolhido como alternativa para avaliar a autonomia energética da horta e a possibilidade de utilizar uma fonte renovável no próprio local.

A instalação proposta utiliza dois módulos de 150 Wp, totalizando 300 Wp, associados a uma bateria LiFePO4 de 100 Ah.

Considerando HSP de projeto de 3,5 e desempenho global de 75%, a geração estimada é de 787,5 Wh/dia, superior ao consumo diário calculado de 584 Wh.

Essa margem é uma estimativa de dimensionamento e não representa garantia de atendimento em qualquer condição climática. O desempenho real depende da orientação, inclinação, sombreamento, temperatura, estado da bateria e condições meteorológicas.


## Limitações da energia solar
A geração depende da disponibilidade de radiação solar. Em períodos prolongados de baixa insolação, a produção pode diminuir e a bateria pode não armazenar energia suficiente para atender a toda a carga.

A bateria também representa um componente importante do investimento inicial e possui vida útil limitada. A substituição da bateria não foi incluída no horizonte financeiro de dez anos, o que pode elevar o custo total real do sistema.

Os painéis e demais componentes precisam de instalação segura, proteção contra intempéries e inspeção periódica. A localização em espaço público também exige atenção à fixação e à proteção contra danos ou furto.

O benefício climático foi estimado considerando apenas as emissões operacionais associadas ao consumo elétrico. As emissões da fabricação, transporte e descarte dos componentes não foram calculadas.


## Custos da alternativa B
| Item | Valor |
|---|---:|
| Dois painéis de 150 Wp | R$ 1.200,00 |
| Bateria LiFePO4 12,8 V / 100 Ah | R$ 1.000,00 |
| Controlador MPPT | R$ 500,00 |
| Materiais e componentes BOS | R$ 600,00 |
| Mão de obra de instalação | R$ 1.000,00 |
| Documentação | R$ 400,00 |
| **CAPEX-base** | **R$ 4.700,00** |
| Reserva para adequações adicionais | R$ 3.500,00 |
| **Investimento inicial total** | **R$ 8.200,00** |
| Conta mensal da distribuidora | R$ 0,00 |
| Manutenção anual estimada | R$ 150,00 |
| Contas em dez anos | R$ 0,00 |
| Manutenção em dez anos | R$ 1.500,00 |
| **Custo total em dez anos** | **R$ 9.700,00** |

A reserva de R$ 3.500,00 é uma premissa preliminar para adequações específicas do local, como base e fixação, abrigo e proteção dos componentes e adequação da passagem de cabos.

O valor precisa ser validado tecnicamente e por orçamento. Deve-se evitar duplicidade com itens já incluídos no BOS ou na mão de obra.

A conta mensal de R$ 0,00 pressupõe que o sistema seja efetivamente isolado off-grid, sem consumo faturado pela distribuidora.

A manutenção anual de R$ 150,00 é uma provisão simplificada para limpeza e inspeção preventiva, com participação comunitária. Não inclui substituição da bateria ou assistência técnica profissional.


## Indicadores ambientais
O consumo anual estimado é de 213,16 kWh.

Com fator médio de emissão de 0,0385 kg CO₂/kWh, as emissões operacionais associadas ao consumo seriam:

213,16 × 0,0385 = **aproximadamente 8,21 kg CO₂/ano**.

Esse valor representa emissões operacionais potencialmente evitadas sob a hipótese de atendimento integral da carga pela geração solar. Não representa o benefício climático líquido do sistema, pois a fabricação, o transporte e o descarte dos componentes não foram contabilizados.


## Referências
ANEEL. Resolução Normativa nº 1.000, de 7 de dezembro de 2021. Disponível em: https://www.rge-rs.com.br/sites/rge-rs/files/2022-04/REN%201000_2021.pdf

EPE. Balanço Energético Nacional 2026, ano-base 2025. Disponível no portal da Empresa de Pesquisa Energética: https://www.epe.gov.br/

IPCC. Climate Change 2014: Mitigation of Climate Change, Anexo III. Disponível em: https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_annex-iii.pdf

IRENA. Renewable power generation costs in 2025. Abu Dhabi: International Renewable Energy Agency, 2026. Disponível em: https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Jul/IRENA_TEC_RPGC_in_2025_2026.pdf

MCTI. Fatores de emissão do Sistema Interligado Nacional. Disponível em: https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-ferramentas/fatores-de-emissao

PINHO, J. T.; GALDINO, M. A. (org.). Manual de Engenharia para Sistemas Fotovoltaicos. Rio de Janeiro: CEPEL/CRESESB, 2014. Disponível em: http://www.cresesb.cepel.br/publicacoes/download/Manual_de_Engenharia_FV_2014.pdf
