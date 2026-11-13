# 08 — Soluções em Energias Renováveis e Sustentáveis
Energia da horta comunitária e do ponto de compostagem: rede elétrica × solar com bateria, cálculos de consumo, diagrama, 3 indicadores e painel.

## Identificação
| Nome | RM |
| --- | --- |
| Anna Luisa Lima | RM575081 |
| Gustavo Fidelis | RM74666 |
| Rafael Meireles | RM574897 |

 ## Descrição do Probelma
Uma horta comunitária localizada na Mooca opera de forma tradicional e colaborativa, dependendo diretamente do manejo manual de mais de 200 voluntários e moradores da região. A irrigação fica sujeita à disponibilidade dos horticultores, enquanto a composteira permanece sem monitoramento adequado de umidade, dependendo da avaliação manual. Essa ausência de automação aumenta os riscos de desperdício de água e outros recursos, falhas na manutenção das plantações e comprometimento da qualidade da compostagem, dificultando a continuidade e a eficiência do canteiro. Uma horta com um sistema inteligente reduzia esses desperdícios e otimizaria o consumo de energia para realizar a irrigação automatizada por meio de uma bomba, monitorar a umidade do solo e o nível da composteira, além de garantir a iluminação noturna do espaço.

 
 ## Solução
O projeto propõe a implantação de uma horta comunitária integrada a um ponto de compostagem, utilizando energia renovável para garantir o funcionamento de atividades essenciais, como irrigação, monitoramento das condições da horta e iluminação noturna. A solução busca automatizar os cuidados com o cultivo, permitindo uma irrigação mais eficiente, o acompanhamento das condições da compostagem e a melhor utilização dos recursos naturais. Além disso, propõe uma gestão energética sustentável, contribuindo para a redução de custos e impactos ambientais. Dessa forma, busca-se promover a autonomia da horta, a produção comunitária de alimentos, a educação ambiental e o envolvimento dos moradores na construção de um espaço público mais sustentável.


## Indicadores usados no dashboard
| Indicador | Valor | Origem |
|---|---|---|
| Consumo | 17,52 kWh/mês | Seção 1 |
| Economia estimada | R$ 22,83/mês | Seção 5 |
| Energia renovável atendida | 100 % | Simulação anual de 365 dias, sem dia de falta de energia |
| CO₂ evitado | 7,6 kg/ano | 198,56 kWh × 0,0385 kg/kWh (MCTI, média anual do SIN em 2023). Com os fatores mensais de 2025 (0,0215 a 0,0289 t/MWh), fica entre 4,3 e 5,7 kg/ano |
| Autonomia da bateria | 1,9 dia | 1.280 Wh × 0,8 / 544 Wh/dia |


## Estrutura do repositório
```
gs-2026-citizentech/
08-energias/
├── README.md                  ← este documento
├── docs/
│   ├── consumo-energetico.md  ← cálculos e justificativas do consumo energético
│   └── fundamentacao-rede-eletrica.md       ← fundamentação teórica com cálculos, benefícios, justificativas, limitações e referências
│   └── fundamentacao-energia-solar.md       ← fundamentação teórica com cálculos, benefícios, justificativas, limitações e
│   └── comparacao-sensibilidade.md       ← comparação de alternativas (custos, consumo, viabilidade, impacto ambiental, vantagens e limitações) e sensibilidades das alternativas
referências
│   └── fontes.md       ← fontes de dados e pesquisa para determinação das premissas
│   └── limitacoes.md       ← limitações identificadas do projeto
```
