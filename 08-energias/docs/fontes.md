# Dados e fontes
Consultas e premissas utilizadas no projeto Ciclo Verde.


## Tarifa e regras da rede
- Tarifa da classe B3, demais classes, da Enel SP: TUSD de R$ 472,42/MWh e TE de R$ 316,96/MWh, total de R$ 789,38/MWh, sem tributos. Resolução Homologatória ANEEL nº 3.596/2026, válida desde 04/07/2026. Disponível em: https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html

- Conferência do valor de R$ 0,78938/kWh sem tributos: https://calculakwh.com.br/artigos/valor-do-kwh-enel-sp/

- Custo de disponibilidade de 30 kWh/mês para ligação monofásica: Resolução Normativa ANEEL nº 1.000/2021. Disponível em: https://www.rge-rs.com.br/sites/rge-rs/files/2022-04/REN%201000_2021.pdf

- Documentação para ligação nova: folder da Enel. Disponível em: https://www.enel.com.br/content/dam/enel-br/para_voce/ligacao_nova/2026/07-julho/AM-0006-26-BTL-FOLDER-LIGACAO-NOVA-RJ-DIGITAL-V03.pdf

- ICMS de 18% e PIS/COFINS de 6%: premissas adotadas pelo grupo para estimar a tarifa com tributos. Os percentuais devem ser conferidos para a situação concreta da unidade consumidora.


## Custos de instalação da rede
- Padrão de entrada monofásico aéreo, SINAPI 101491, R$ 1.951,37 sem o poste (AF_12/2025). Disponível em: https://orcamentor.com/composicao/101491/

- Faixa de mercado do padrão monofásico em 2026, de R$ 1.800,00 a R$ 3.000,00. Disponível em: https://monitordomercado.com.br/noticias/410146-quanto-custa-trocar-o-padrao-de-entrada-de-energia-para-suportar-os-novos-aparelhos-da-casa/

- Instalação do padrão, R$ 2.500,00: premissa orçamentária adotada pelo grupo, baseada nas referências de custo consultadas. Sem cotação formal.

- Equipamentos, R$ 1.000,00: estimativa do grupo.

- Documentação, R$ 1.200,00: estimativa do grupo, sujeita à validação conforme as exigências aplicáveis.

- Circuito interno até a horta, R$ 800,00: estimativa do grupo para o cenário A2, em que já existe um ponto de energia próximo.

- Manutenção e reposição da infraestrutura elétrica interna, R$ 630,00 por ano: provisão estimada pelo grupo para inspeções, reparos e reserva para substituição de componentes. Não é tarifa da distribuidora nem orçamento formal. Deve ser validada por avaliação técnica e cotação.


## Custos de instalação solar
- Painéis de 150 Wp, dois módulos, total de R$ 1.200,00: estimativa do grupo com base em anúncios de mercado. Referência de busca: https://lista.mercadolivre.com.br/placas-para-energia-solar-avulsa

- Controlador MPPT, R$ 500,00: referência de produto consultado em https://www.neosolar.com.br/loja/controlador-carga-mppt-40a-12-24v-epever-xtra-4210n.html

- Bateria LiFePO4 12 V, R$ 1.000,00: estimativa do grupo. Referência de mercado: https://br.ebay.com/b/Lithium-Iron-Phosphate-LiFePO-4-12-V-Rechargeable-Batteries/48619/bn_7116771597

- Fusíveis, cabos, conectores, suporte, caixa e conversor, R$ 600,00: estimativa do grupo para materiais e componentes BOS, sem cotação formal.

- Mão de obra de instalação solar, R$ 1.000,00: premissa orçamentária adotada pelo grupo, sem cotação formal.

- Documentação solar, R$ 400,00: estimativa do grupo.

- Adequações adicionais de infraestrutura solar, R$ 3.500,00: reserva preliminar para base e fixação, abrigo e proteção dos componentes e adequação da passagem de cabos. Valor adotado como premissa do projeto, ainda sem orçamento formal e sujeito a validação técnica. Deve-se evitar sobreposição com itens já incluídos no BOS ou na mão de obra.

- Manutenção solar, R$ 150,00 por ano: provisão simplificada do grupo para limpeza e inspeção preventiva, sem orçamento formal. Não contempla substituição da bateria ou assistência técnica profissional.


## Emissões
- Fator médio do SIN em 2023, 38,5 kg CO₂/MWh. Fonte de consulta: https://eixos.com.br/brasil-tem-menor-taxa-de-emissao-de-carbono-na-geracao-eletrica-em-onze-anos/

- Tabelas oficiais de fatores de emissão: Ministério da Ciência, Tecnologia e Inovação. Disponível em: https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-ferramentas/fatores-de-emissao

- Fatores mensais de 2025: https://canalsolar.com.br/emissoes-de-co₂-geracao-eletrica-mcti/


## Recurso solar
- Desempenho global PR = 0,75 e inclinação de referência para São Paulo: material do curso IEE0004, USP. Disponível em: https://edisciplinas.usp.br/pluginfile.php/6848059/mod_resource/content/5/undefined/Curso_IEE0004_Aula_11_2022_1.pdf

- HSP de projeto de 3,5 e média anual de 4,5 kWh/m²·dia: valores estimados pelo grupo. O perfil mensal usado na simulação é sintético. A conferir no SunData/CRESESB com as coordenadas da horta: https://cresesb.cepel.br/sundata/


## Dados simulados
O arquivo `dash/calculos.py` gera a série diária de geração, bateria, umidade do solo e acionamento da bomba com semente fixa (42). São dados sintéticos para demonstrar a lógica de automação, sem medição real.
