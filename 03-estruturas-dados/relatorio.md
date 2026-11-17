# Mapa dos Pontos Viciados: relatório técnico

**GS 2026.2 · Data Structures and Algorithms · Turma 1CCPR · Trio Ciclo Verde**
Gustavo Fidelis de Souza e Silva (RM 574666) · Rafael Meirelles (RM 574897) · Anna Luisa Lima (RM 575081)

## 1. O problema urbano

O PDF da disciplina dá como exemplos de ocorrência urbana "buraco, iluminação, lixo, enchente, entre outros". O trio escolheu um desses problemas, o **descarte irregular de lixo**, e aprofundou nele. Em vez de categorias gerais, o sistema separa os tipos de lixo: entulho de obra, lixo doméstico, móveis velhos, pneus, poda de árvore, eletrônicos e outros. É o mesmo tema do trio nas outras matérias da GS, o Ciclo Verde.

Na região da Mooca, o lixo jogado na rua volta sempre para os mesmos lugares, os "pontos viciados". Em julho de 2026, a Subprefeitura Mooca, que cuida dos distritos Mooca, Água Rasa, Belém, Tatuapé, Pari e Brás, fez uma mobilização contra o descarte ilegal de entulho e lixo. Segundo a reportagem, já foi preciso limpar a mesma rua três vezes num único dia (Folha VP, 2026). Limpar de novo não resolve: se o lixo volta, o lugar precisa de outra ação, como uma placa, uma câmera ou um ecoponto perto.

## 2. Justificativa da solução

Sem organizar as reclamações, ninguém sabe onde o lixo mais volta nem há quanto tempo ele está na rua. O sistema registra cada ocorrência com o tipo de lixo, o bairro, o local, quantas vezes o lixo voltou depois de limpo e há quantos dias está lá. Com isso, monta um ranking e estatísticas que mostram onde agir primeiro.

Fizemos o sistema no console, porque o PDF não exige interface gráfica e o foco da avaliação são os conteúdos da disciplina.

## 3. Estrutura dos dados

Os dados ficam em **6 vetores paralelos**. A posição `i` de todos os vetores é a mesma ocorrência.

| Vetor | Tipo | Exemplo (posição 0) |
| --- | --- | --- |
| `ids` | texto | `"OC-001"` |
| `categorias` | texto | `"Entulho de obra"` |
| `bairros` | texto | `"Brás"` |
| `referencias` | texto | `"embaixo do viaduto"` |
| `vezes_que_voltou` | inteiro | `6` |
| `dias_em_aberto` | inteiro | `40` |

Dois vetores fixos guardam as opções válidas: `CATEGORIAS` (7 tipos de lixo) e `BAIRROS` (6 bairros). O sistema pode começar com 18 ocorrências de exemplo. Elas são **dados simulados**, não registros reais. Os dados ficam só na memória enquanto o programa está aberto.

## 4. Algoritmos

**Busca sequencial.** A função `busca_sequencial` percorre o vetor da primeira à última posição, compara cada valor com o procurado e guarda as posições onde encontrou. A mesma função serve para buscar por tipo de lixo, por bairro e para contar os registros de um mesmo local. Com *n* ocorrências, ela faz *n* comparações. O tipo e o bairro são escolhidos por número, então não há erro de digitação nem de acento.

**Ordenação por seleção.** A função `ordenar_por_selecao` procura, entre as ocorrências que sobraram, a que deve vir primeiro e a troca com a posição da vez. Depois repete com o resto. Dois cuidados:
- ela ordena **cópias** dos vetores, para não mudar a ordem do cadastro;
- quando troca as posições `i` e `j`, troca nos **6 vetores juntos**. Assim os dados de uma ocorrência não se misturam com os de outra.

Há dois critérios, na mesma função:
- **reincidência**, do maior para o menor. No empate, vem primeiro quem tem mais dias em aberto;
- **dias em aberto**, do maior para o menor. No empate, vem primeiro quem tem mais reincidência.

A reincidência é o critério principal porque mostra onde só limpar não basta. Se tudo empatar, vem primeiro o cadastro mais antigo.

**Seleção × bolha.** Para comparar, o sistema também ordena pela bolha (`ordenar_por_bolha`), que compara vizinhos e troca os que estão fora de ordem. Com os 18 exemplos, as duas chegam à mesma ordem, mas a seleção fez 153 comparações e a bolha fez 143. A bolha fez menos porque para assim que uma passada inteira não troca nada, ou seja, quando a lista já ficou em ordem antes do fim. A seleção não tem esse atalho e faz sempre *n* × (*n* − 1) ÷ 2 comparações (18 × 17 ÷ 2 = 153), mesmo se a lista já estiver ordenada.

**Contadores e acumuladores.**
- Contadores: `contar_por_opcao` conta as ocorrências de cada tipo e de cada bairro, `pontos_viciados` conta os lugares onde o lixo voltou 3 vezes ou mais, e `comparacoes` conta o trabalho de cada ordenação.
- Acumuladores: `soma_dias` e `soma_voltas` somam os valores de todas as ocorrências, e as médias saem dessas somas.
- O bairro e o tipo de lixo mais comuns são encontrados com um laço que guarda o maior valor; se houver empate, o sistema mostra todos.

**Validação da entrada.**
- `ler_inteiro` confere caractere por caractere se o texto só tem algarismos e se o número está dentro do limite.
- `ler_texto` recusa texto vazio ou com mais de 60 caracteres.
- `ler_sim_nao` só aceita sim ou não.

Em todos os casos, o sistema pergunta de novo até receber um valor válido.

## 5. Funcionalidades

| Opção | O que faz |
| --- | --- |
| 1) Cadastrar | Registra a ocorrência e avisa se o lugar é um ponto viciado (3 registros ou mais no mesmo local, ou lixo que já voltou 3 vezes ou mais), dizendo o motivo |
| 2) Listar | Mostra todas as ocorrências numa tabela |
| 3) e 4) Buscar | Por tipo de lixo ou por bairro, com busca sequencial |
| 5) Ranking | Ordena por reincidência ou por dias em aberto |
| 6) Estatísticas | Total, médias, pontos viciados, contagem por tipo e bairro, mais comuns |
| 7) Comparar | Seleção × bolha, com o número de comparações |

Com os 18 exemplos (simulados):
- o Brás é o bairro com mais ocorrências (5);
- o entulho de obra é o tipo mais comum (5);
- 10 dos 18 pontos já voltaram 3 vezes ou mais;
- o lixo fica em média 21,3 dias no lugar.

## 6. Diagrama de atividades

O diagrama de atividades (UML) é entregue à parte, no arquivo `diagrama_atividades.png`, em tamanho grande para ser lido. O fluxo começa na escolha dos dados de exemplo e passa pelo menu.
- **Cadastro:** guarda a ocorrência nos vetores e decide se mostra o alerta.
- **Consulta e análise (opções 2 a 7):** primeiro conferem se há ocorrências; depois listam, buscam, ordenam ou calculam as estatísticas.
- **Volta ao menu:** todo caminho termina na mesma junção, até a pessoa escolher sair.

## 7. Principais desafios

- **Manter os vetores alinhados.** Na ordenação, trocar a posição em um só vetor misturaria as ocorrências. A função `trocar` faz a troca nos 6 vetores de uma vez.
- **Não estragar a ordem do cadastro.** O ranking ordena cópias dos vetores, e a listagem continua na ordem em que as ocorrências entraram.
- **Empates no ranking.** Muitos pontos têm o mesmo número de voltas. Definimos um desempate (dias em aberto) e, no fim, o id.
- **Entrada errada.** Letra no lugar de número, número negativo e texto vazio quebravam a leitura. A solução foi conferir o texto antes de converter e escolher tipo e bairro por número.
- **Lista vazia.** A média dividiria por zero. As opções de consulta conferem antes se há ocorrências.

## 8. Benefícios para a comunidade

Para o morador, registrar um problema se resume a cinco informações: tipo de lixo, bairro, local, quantas vezes ele voltou depois de limpo e há quantos dias está lá. Quando o local já tem três registros, ou o lixo já voltou três vezes, o sistema avisa na hora que é um ponto viciado e diz o motivo, o que mostra que o problema já tinha sido apontado.

Para a subprefeitura, o ganho está em saber onde olhar primeiro. O ranking por reincidência coloca no topo os lugares onde o lixo mais volta, e o ranking por dias em aberto mostra o que está parado há mais tempo. A diferença pesa na decisão: um ponto que voltou cinco vezes pede outra medida, como placa, câmera ou ecoponto por perto, e mandar a equipe de limpeza de novo só repete o gasto. As estatísticas por tipo de lixo e por bairro ajudam no planejamento, já que o predomínio de entulho de obra numa região indica falta de um lugar próximo para descartá-lo, e isso se resolve de outro jeito que um problema de lixo doméstico.

Para a região, a vantagem é ter o problema registrado em dados que podem ser consultados, comparados e atualizados, em vez de depender de memória ou de reclamações soltas. A versão atual guarda os dados só na memória e usa registros simulados nos exemplos, então esses benefícios valem para o sistema alimentado com ocorrências reais. O passo seguinte é gravar os dados em arquivo ou banco e ligar os pontos de lixo orgânico à compostagem e à horta do Ciclo Verde.

## 9. Uso de IA

- **Claude Code (Anthropic):** montou o checklist do PDF e escreveu o rascunho do código, dos roteiros de teste, do diagrama e deste relatório.
- **Decisões do projeto:** foram aprovadas pelo Fidelis, que conferiu o checklist e os testes com a ajuda do Claude (chat). São elas: as categorias, os vetores paralelos, os critérios de ordenação, os dois motivos do alerta e o "0" para sair.

## 10. O que cada um fez

| Integrante | O que fez |
| --- | --- |
| Gustavo Fidelis de Souza e Silva | Definiu as decisões do projeto (categorias, vetores paralelos, critérios de ordenação e alerta), conferiu o código e os testes feitos com o Claude Code e apresenta o vídeo de demonstração |
| Rafael Meirelles | [FIDELIS: preencher o que o Rafael fez] |
| Anna Luisa Lima | Escreveu a seção 8, sobre os benefícios para a comunidade |

## Referências

- Folha VP. *SUB-MO: mobilização contra o descarte ilegal de entulho e lixo*. 24 jul. 2026. Disponível em: https://folhavponline.com.br/acontece-na-regiao/sub-mo-faz-mobilizacao-contra-o-descarte-irregular-de-entulho-e-lixo/
- FIAP. *Global Solution 2026.2: Data Structures and Algorithms* (enunciado da disciplina).
