# 08 — Soluções em Energias Renováveis e Sustentáveis
Energia da horta comunitária e do ponto de compostagem: rede elétrica × solar com bateria, cálculos de consumo, diagrama, 3 indicadores e painel.

## Identificação
| Nome | RM |
| --- | --- |
| Anna Luisa Lima | 575081 |
| Gustavo Fidelis de Souza e Silva | 574666 |
| Rafael Meirelles | 574897 |

## Descrição do problema
Uma horta comunitária localizada na Mooca opera de forma tradicional e colaborativa, dependendo diretamente do manejo manual de mais de 200 voluntários e moradores da região. A irrigação fica sujeita à disponibilidade dos horticultores, enquanto a composteira permanece sem monitoramento adequado de umidade, dependendo da avaliação manual. Essa ausência de automação aumenta os riscos de desperdício de água e outros recursos, falhas na manutenção das plantações e comprometimento da qualidade da compostagem, dificultando a continuidade e a eficiência do canteiro. Uma horta com um sistema inteligente reduzia esses desperdícios e otimizaria o consumo de energia para realizar a irrigação automatizada por meio de uma bomba, monitorar a umidade do solo e o nível da composteira, além de garantir a iluminação noturna do espaço.

 
## Solução
O projeto propõe a implantação de uma horta comunitária integrada a um ponto de compostagem, utilizando energia renovável para garantir o funcionamento de atividades essenciais, como irrigação, monitoramento das condições da horta e iluminação noturna. A solução busca automatizar os cuidados com o cultivo, permitindo uma irrigação mais eficiente, o acompanhamento das condições da compostagem e a melhor utilização dos recursos naturais. Além disso, propõe uma gestão energética sustentável, contribuindo para a redução de custos e impactos ambientais. Dessa forma, busca-se promover a autonomia da horta, a produção comunitária de alimentos, a educação ambiental e o envolvimento dos moradores na construção de um espaço público mais sustentável.

![Diagrama conceitual](fig/diagrama_conceitual.jpg)
*Comparamos essa solução com a ligação à rede da Enel (classe tarifária B3, demais classes) para a mesma carga, em 10 anos.*



## Indicadores usados no dashboard
| Indicador | Valor | Origem |
|---|---:|---|
| Consumo energético | 17,52 kWh/mês | Equipamentos e período de 30 dias |
| Economia operacional estimada | R$ 10,33/mês | Diferença entre conta da rede e custos operacionais solares, incluindo manutenção |
| Energia renovável atendida | Resultado da simulação | Simulação anual de geração, bateria e consumo |
| Emissões operacionais potencialmente evitadas | 8,21 kg CO2/ano | 213,16 kWh × 0,0385 kg CO2/kWh |
| Autonomia da bateria | 1,75 dia | 1.280 Wh × 0,8 / 584 Wh/dia |


## Comparação financeira
| Indicador | Rede elétrica | Solar |
|---|---:|---:|
| Investimento inicial | R$ 4.700,00 | R$ 5.400,00 |
| Conta mensal | R$ 31,16 | R$ 8,33 |
| Manutenção anual | R$ 0,00 | R$ 150,00 |
| Custo acumulado em 10 anos | R$ 8.439,20 | R$ 7.899,60 |

A alternativa solar apresenta investimento inicial R$ 700,00 maior, mas custo acumulado estimado R$ 539,60 menor em dez anos, na comparação com uma nova ligação à rede.

A reserva técnica solar e a manutenção são estimativas sujeitas à validação por cotação.


## Como executar o projeto
### 1. Clone o repositório:
```bash
git clone https://github.com/Fidelisss07/gs-2026-2-citizentech.git
```

### 2. Entre na pasta do projeto:
```bash
cd gs-2026-2-citizentech
cd 08-energias
```

### 3. Instale as dependências
Certifique-se de ter o Python e o pip instalados. Execute o comando abaixo para instalar todas as bibliotecas necessárias:
```bash
pip install "streamlit>=1.30" pandas numpy matplotlib
```

### 4. Executar o projeto
**Dashboard interativo (Streamlit):**
```bash
streamlit run dash/dashboard.py
```

**Executar os cálculos no terminal:**
```bash
python dash/calculos.py
```

**Gerar ou atualizar as figuras:**
```bash
python dash/gerar-figuras.py
```

## Estrutura do repositório
```
gs-2026-2-citizentech/
08-energias/
├── README.md                  ← este documento
├── dash/
│   ├── calculos.py  ← todas as formulas de calculos
│   ├── dashboard.py  ← dashboard que copia as premissas do JSON, sobrescreve e chama tudo com os valores novos.
│   ├── gerar-figuras.py  ← gera imagens a partir dos valores do dashboard
├── entrega_SERS.txt  ← arquivo de entrega no portal (nomes, RMs e links)
├── data/
│   ├── equipamentos.csv  ← armazenamento de todos os dados dos equipamentos
│   ├── premissas.json  ← armazenamento de todos os dados que não são equipamentos
├── docs/
│   ├── consumo-energetico.md  ← cálculos e justificativas do consumo energético
│   └── fundamentacao-rede-eletrica.md       ← fundamentação teórica com cálculos, benefícios, justificativas, limitações e referências
│   └── fundamentacao-energia-solar.md       ← fundamentação teórica com cálculos, benefícios, justificativas, limitações e
│   └── comparacao-sensibilidade.md       ← comparação de alternativas (custos, consumo, viabilidade, impacto ambiental, vantagens e limitações) e sensibilidades das alternativas
│   └── fontes.md       ← fontes de dados e pesquisa para determinação das premissas
│   └── limitacoes.md       ← limitações identificadas do projeto
├── fig/
│   ├── diagrama_conceitual.jpg  ← diagrama conceitual de funcionamento do projeto
```
