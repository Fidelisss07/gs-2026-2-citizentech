# Alternativa B: energia solar fotovoltaica 
Este texto justifica a escolha da fonte renovável da alternativa A. Os números do projeto vêm de `docs/consumo-energetico.md`. Os dados de contexto (custos globais, matriz brasileira, emissões) estão nas fontes listadas ao final.

## Dimensionamento solar
- Parâmetros: HSP de projeto 3,5 kWh/m²·dia (mês mais fraco do inverno paulistano, com folga para sombra de prédios vizinhos), desempenho global PR = 0,75, bateria LiFePO4 com profundidade de descarga de 80 % e autonomia alvo de 1,5 dia.
- Potência mínima do painel: P = 544 / (3,5 × 0,75) = 207,2 Wp. Adotado: 2 módulos de 150 Wp (300 Wp).
- Energia gerada: em média anual (HSP 4,5) o painel entrega 300 × 4,5 × 0,75 = 1.012,5 Wh/dia; no pior mês, 300 × 3,5 × 0,75 = 787,5 Wh/dia, 30% acima do consumo.
- Capacidade mínima da bateria: 544 × 1,5 / 0,8 = 1.020 Wh, ou 79,7 Ah a 12,8 V. Adotada: 12,8 V, 100 Ah (1.280 Wh), que dá 1.280 × 0,8 / 544 = 1,88 dia de autonomia com 80 % de descarga.
- Controlador: a corrente de 300 Wp em 12,8 V chega a cerca de 23,4 A. Adotado MPPT de 40 A, com folga.


## Benefícios da energia
A energia solar atende a demanda de 17,52 kWh por mês para uma bomba, um sensor e duas luminárias no próprio local, sem estender rede, sem solicitar ligação e sem combustível. O Manual de Engenharia para Sistemas Fotovoltaicos do CEPEL/CRESESB apresenta a tecnologia justamente como opção para levar energia a quem a rede não atende e para manter uma matriz elétrica apoiada em fontes renováveis. Um painel de 150 Wp com bateria de 100 Ah cobre a carga mesmo no mês de menor insolação, com folga de cerca de 20% na geração.

Esse arranjo muda a rotina do espaço. A bomba passa a ligar quando o sensor indica terra seca, e a rega deixa de depender de alguém estar presente. As luminárias permitem uso da horta à noite. Como o sistema opera em 12V de corrente contínua, o risco elétrico para voluntários é menor do que numa instalação de 127V ou 220V, e não há ruído nem emissão local, o que combina com um espaço de cultivo e compostagem.

A escolha é assertiva financeiramente. Ao invés de pagar R$8.439,20 em 10 anos, o gasto estimado na rede solar é de R$6.699,60. Dividindo pelos 2.102,40 kWh (17,52 * 120) efetivamente consumidos, o custo médio fica em torno de R$4,01 por kWh na rede e R$3,18 por kWh no solar.
*Cálculo ilustrativo do grupo.*


## Justificativa da escolha da energia
O custo da geração solar caiu de forma contínua. Segundo a IRENA, o custo nivelado médio mundial da energia solar fotovoltaica foi de US$44/MWh em 2025, e mais de 90% dos projetos renováveis de grande porte comissionados naquele ano entregaram energia mais barata que a usina fóssil nova mais barata do mesmo mercado. Desde 2010, o custo do solar caiu 89%. Os sistemas com bateria seguem a mesma direção: o custo instalado de baterias de grande porte caiu cerca de 30% em 2025, e a energia firme de solar com armazenamento ficou abaixo de US$85/MWh em locais de boa insolação. Esses números descrevem usinas grandes, e um sistema de 150 Wp custa mais por kWh. Eles mostram a tendência da tecnologia, não o preço da horta.

No Brasil, a fonte já faz parte do planejamento. O Balanço Energético Nacional 2026, ano-base 2025, registra que 86,8% da matriz elétrica é renovável, com a solar em 11,4% da geração. A expansão da solar distribuída é um dos eixos das projeções de longo prazo da EPE, que preveem a geração distribuída perto de 78 GW em 2035.

O solar também dá autonomia. Com bateria, a irrigação continua durante uma queda da rede, e a comunidade deixa de depender da distribuidora, de documentação de ligação e de reajuste tarifário. O projeto se liga ao Objetivo de Desenvolvimento Sustentável 7, energia limpa e acessível, da Agenda 2030 da ONU.


## Limitações da energia
O ganho climático deste projeto é pequeno. O fator médio da rede brasileira foi de 0,0385 tCO₂/MWh em 2023, então a horta emitiria cerca de 4,3kg de CO₂ por ano na rede. A fonte solar tem emissões de ciclo de vida, que vêm sobretudo da fabricação: o IPCC aponta mediana de 41 gCO₂eq/kWh para solar em telhado e 48 gCO₂eq/kWh para usinas solares, contra 820 do carvão e 490 do gás natural.
Aplicadas aos 204,40 kWh anuais, essas medianas dão entre 8,38 e 9,81kg por ano, e a bateria não está nesses números.
A vantagem climática do solar aparece quando ele substitui geração fóssil, e no Brasil isso depende do momento: a geração termelétrica cresceu 12,3% em 2025, para 169,9 TWh.

A produção cai no inverno e em sequências de dias nublados, e por isso o sistema depende de bateria, que encarece a instalação e tem vida útil menor que a do painel. O destino final de painel e bateria precisa de plano. E o painel exposto na rua exige fixação segura contra furto.

Sendo assim, o projeto sustenta a escolha do solar em custo, autonomia, simplicidade de implantação e valor educativo, e trata o benefício de CO₂ como pequeno e dependente de premissas.


## Custos
| Item | R$ |
|---|---|
| Painel 150 Wp | 1.200,00 |
| Conta mensal | 8,33 |
| Controlador MPPT 30 A | 500,00 |
| Bateria LiFePO4 12,8 V 100Ah | 1.000,00 |
| Fusíveis, cabos, MC4, suporte, caixa, conversor 12→5 V | 600,00 |
| Mão de obra de instalação | 1.000,00 |
| Manutenção anual - limpeza e inspeção | 1.000,00 |
| Documentação | 400,00 |
| Total | 5.708,33 |


## Referências
ANEEL. Resolução Normativa nº 1.000, de 7 de dezembro de 2021. Disponível em: https://www.rge-rs.com.br/sites/rge-rs/files/2022-04/REN%201000_2021.pdf

EPE. Balanço Energético Nacional 2026, ano-base 2025, Relatório Síntese. Dados consultados em reportagens sobre o relatório: https://canalsolar.com.br/geracao-termeletrica-cresce-matriz-eletrica/ e https://capitaldigital.com.br/ia-devora-eletricidade-na-asia-e-antecipa-desafio-bilionario-para-o-redata/ (completar com o PDF oficial da EPE antes da entrega)

EPE. Plano Decenal de Expansão de Energia (projeção da geração distribuída em 78 GW em 2035), conforme reportagem: https://canalsolar.com.br/matriz-eletrica-brasileira-projecao-governo-2035/ (completar com o documento oficial da EPE)

IPCC. Climate Change 2014: Mitigation of Climate Change, Anexo III (emissões de ciclo de vida). Disponível em: https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_annex-iii.pdf

IRENA. Renewable power generation costs in 2025. Abu Dhabi: International Renewable Energy Agency, 2026. Disponível em: https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Jul/IRENA_TEC_RPGC_in_2025_2026.pdf

MCTI. Fator médio de emissão do SIN, média anual de 2023 (0,0385 tCO₂/MWh). Disponível em: https://eixos.com.br/brasil-tem-menor-taxa-de-emissao-de-carbono-na-geracao-eletrica-em-onze-anos/
ONU. Agenda 2030 para o Desenvolvimento Sustentável, ODS 7 (completar com o link do portal da ONU Brasil).

PINHO, J. T.; GALDINO, M. A. (org.). Manual de Engenharia para Sistemas Fotovoltaicos. Rio de Janeiro: CEPEL/CRESESB, 2014. Disponível em: http://www.cresesb.cepel.br/publicacoes/download/Manual_de_Engenharia_FV_2014.pdf
