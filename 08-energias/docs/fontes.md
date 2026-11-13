# Dados e fontes
Consultas feitas em 12/11/2026.

## Tarifa e regras da rede
- Tarifa da classe B3, demais classes, da Enel SP - TUSD R$ 472,42/MWh e TE R$ 316,96/MWh, total R$ 789,38/MWh; mínimo mensal monofásico de R$ 23,68, (ANEEL 3.596/2026, desde 04/07/2026): https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html
  
- Conferência do valor R$ 0,78938/kWh sem tributos: https://calculakwh.com.br/artigos/valor-do-kwh-enel-sp/
  
- Custo de disponibilidade de 30 kWh/mês para ligação monofásica: Resolução Normativa ANEEL 1.000/2021.
  
- Documentação para ligação nova: folder da Enel https://www.enel.com.br/content/dam/enel-br/para_voce/ligacao_nova/2026/07-julho/AM-0006-26-BTL-FOLDER-LIGACAO-NOVA-RJ-DIGITAL-V03.pdf
  
- ICMS de 18% e PIS/COFINS de 6%: premissa do grupo para a classe B3 (não residencial).


## Custos de instalação
- Padrão de entrada monofásico aéreo, SINAPI 101491, R$ 1.951,37 sem o poste (AF_12/2025): https://orcamentor.com/composicao/101491/
  
- Faixa de mercado do padrão monofásico em 2026, de R$ 1.800 a R$ 3.000: https://monitordomercado.com.br/noticias/410146-quanto-custa-trocar-o-padrao-de-entrada-de-energia-para-suportar-os-novos-aparelhos-da-casa/
  
- Painel de 150Wp (adotados dois), anúncios média de R$600: https://lista.mercadolivre.com.br/placas-para-energia-solar-avulsa
  
- Controlador MPPT, R$500,00: https://www.neosolar.com.br/loja/controlador-carga-mppt-40a-12-24v-epever-xtra-4210n.html?utm_source=google&utm_medium=cpc&utm_campaign=pm-powerstation&utm_term=powerstation&utm_content=&gad_source=1&gad_campaignid=24388815098&gbraid=0AAAAADml2s2QcafFeVkEcNEoWBHy0Jqyb&gclid=Cj0KCQiAh9vXBhDKARIsAMooYhfJq1ImHo8MtLBT8vkT0X_dXyRkfVkSK5Pq0p2UXbrmlWNmelvlOFwaAmlwEALw_wcB
  
- Bateria LiFePO4 12V: média de R$1.000,00: https://br.ebay.com/b/Lithium-Iron-Phosphate-LiFePO-4-12-V-Rechargeable-Batteries/48619/bn_7116771597
  
- Fusíveis, cabos, conectores, suporte, caixa e conversor (R$ 600), mão de obra (R$ 400) e circuito até a horta (R$ 800): estimativas do grupo, sem cotação.


## Emissões
- Fator médio do SIN em 2023, 38,5 kg CO₂/MWh (MCTI): https://eixos.com.br/brasil-tem-menor-taxa-de-emissao-de-carbono-na-geracao-eletrica-em-onze-anos/
  
- Fatores mensais de 2025 (21,5 a 28,9 kg CO₂/MWh no primeiro quadrimestre): https://canalsolar.com.br/emissoes-de-co₂-geracao-eletrica-mcti/
  
- Tabelas oficiais: https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-ferramentas/fatores-de-emissao

## Recurso solar
- Desempenho global PR = 0,75 e inclinação ótima de 23° para São Paulo, orientada ao norte (material do curso IEE0004, USP): https://edisciplinas.usp.br/pluginfile.php/6848059/mod_resource/content/5/undefined/Curso_IEE0004_Aula_11_2022_1.pdf

- HSP de projeto 3,5 e média anual de 4,5 kWh/m²·dia: valores estimados pelo grupo. O perfil mensal usado na simulação é sintético. A conferir no SunData/CRESESB com as coordenadas da horta: https://cresesb.cepel.br/sundata/

## Dados simulados

`src/calculos.py` gera a série diária de geração, bateria, umidade do solo e bomba com semente fixa (42). São dados sintéticos para demonstrar a lógica de automação, sem medição real.
