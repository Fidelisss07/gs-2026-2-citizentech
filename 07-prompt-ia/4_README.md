# Ciclo Verde: assistente de descarte da região da Mooca

**GS 2026.2 · Prompt and Artificial Intelligence · Prof. Jorge Luiz Gomes**
**Turma 1CCPR · Trio · Frente B: Descarte e sustentabilidade**

| Integrante | RM |
| --- | --- |
| Gustavo Fidelis de Souza e Silva | 574666 |
| Rafael Meirelles | 574897 |
| Ana | 575081 |

## O problema

O lixo jogado na rua volta sempre para os mesmos lugares. Em julho de 2026, a Subprefeitura Mooca fez uma ação contra os "pontos viciados" de lixo e entulho na região, e houve rua limpa 3 vezes no mesmo dia ([Folha VP](https://folhavponline.com.br/acontece-na-regiao/sub-mo-faz-mobilizacao-contra-o-descarte-irregular-de-entulho-e-lixo/)).

Muita gente joga lixo na rua porque não sabe onde descartar, o que o ponto aceita ou se ele está aberto. A informação existe, mas não chega ao morador.

## O que fizemos

Um assistente que responde ao morador da Mooca, Água Rasa, Belém, Brás e Tatuapé:

- onde levar cada tipo de lixo;
- o que cada ponto aceita e não aceita;
- se o ponto está aberto, lotado ou interditado;
- qual o ponto alternativo quando um está lotado.

**Exemplo:**
> **Morador:** Posso levar um sofá velho no ecoponto da Mooca hoje?
> **Assistente:** Sim. O ecoponto da Mooca (lugar que recebe entulho e móveis de graça) aceita sofá e está aberto hoje até as 17h. (baseado no registro FZC-004)

O assistente responde só com base nos 12 registros do `2_dados_servico.json`. Quando a informação não está nos dados, ele diz isso e indica o 156.

## Arquivos da entrega

| Arquivo | O que é |
| --- | --- |
| `1_Notebook_GS2026_2.ipynb` | O notebook, com as seções 0 a 7. Roda de cima a baixo no Colab |
| `2_dados_servico.json` | Os 12 pontos de descarte (dados simulados), gravados pelo próprio notebook |
| `3_prompts_kit.md` | System prompt final, versões v1 e v2, few-shot, prompt do enriquecimento e registro de iterações |
| `4_README.md` | Este arquivo |
| `5_certificacao.txt` | Tela final do notebook, links, nomes e RMs |
| `6_Chat_Log.txt` | Registro do uso de IA durante o trabalho |

## Como executar

1. Abra o `1_Notebook_GS2026_2.ipynb` no [Google Colab](https://colab.research.google.com).
2. (Opcional, bem mais rápido) Em **Ambiente de execução → Alterar o tipo de ambiente de execução**, escolha **GPU T4**.
3. Clique em **Ambiente de execução → Executar tudo** (Runtime → Run all). A primeira parte instala o Ollama e baixa o modelo, o que leva uns 2 minutos. Na CPU, o notebook inteiro leva cerca de 30 minutos.
4. O notebook grava o `2_dados_servico.json` na pasta do Colab (ícone de pasta). Baixe o arquivo.

**Por que o Ollama roda dentro do Colab:** o PDF pede o `llama3.2:1b` no Ollama Cloud, mas esse modelo não está disponível lá; por isso o notebook roda o mesmo modelo com o Ollama dentro do Colab. Não usa API paga nem chave de API.

Se o Colab cair no meio, rode tudo de novo. Se uma chamada ao modelo falhar, o notebook não para: a regra fixa da Seção 3 assume e a resposta fica marcada como erro na tabela.

## Prints

As imagens ficam na pasta `07-prompt-ia/prints` do [repositório do trio](https://github.com/Fidelisss07/gs-2026-2-citizentech).

| O que mostra | Print |
| --- | --- |
| Run all concluído (Seção 1) | `prints/01-run-all.png` |
| Relato original × resumo da IA (Seção 2) | `prints/02-enriquecimento.png` |
| Tabela de auditoria com a coluna `fonte` (Seção 3) | `prints/03-auditoria.png` |
| Matriz 5 × 2 com as notas do trio (Seção 5) | `prints/05-matriz.png` |
| Tela final (Seção 7) | `prints/07-tela-final.png` |

## Decisões técnicas

- **Frente B.** O tema do trio é o lixo do bairro, e a frente B é a que fala de descarte.
- **Ollama dentro do Colab.** No Ollama Cloud, o `llama3.2:1b` dá erro 404 (modelo não encontrado), e os modelos que existem lá pedem créditos pagos (erro 402). O PDF pede esse modelo e não permite API paga. Por isso o notebook instala o Ollama no próprio Colab e roda o mesmo `llama3.2:1b`, sem chave.
- **Dados simulados com erros de propósito.** Os dados brutos têm `acessivel` escrito como texto, horários em formatos diferentes, um ponto lotado sem motivo e um id repetido. Assim as 4 regras de negócio têm o que corrigir, e o notebook mostra quantas correções fez.
- **Onde ficam as 4 regras.** O PDF fala da Seção 3 num lugar e da Seção 1 em outro. Aplicamos as regras na Seção 1, antes de gravar o JSON, e conferimos de novo na Seção 3, relendo o arquivo gravado.
- **Regra 1.** O texto da regra 1 no PDF diz o contrário da tabela do esquema. Seguimos a tabela: status diferente de `ativo` precisa de motivo.
- **Horário.** "24h" não é uma hora e "08:00" é texto. Por isso todo horário vira um formato só e a função `esta_aberto()` compara em minutos. Nos testes a hora da consulta é fixa (10:00), para o resultado poder ser repetido.
- **Temperatura 0.1.** Para classificar e responder, queremos a mesma saída para a mesma entrada, e não criatividade.
- **Validação e regra fixa.** A resposta da IA só vale se a urgência for `urgente`, `atencao` ou `ok`, nenhum campo vier vazio e o resumo tiver até 140 caracteres. Se falhar, a regra fixa decide.
- **Limpeza da urgência.** No primeiro teste, o modelo escreveu "atenção", "Atenção" e até "atenuada", e 8 de 12 respostas caíram na regra fixa. Agora tiramos acentos e espaços e passamos para minúsculas antes de comparar. "Atenção" vira `atencao` e é aceita; palavras que não são `urgente`, `atencao` ou `ok`, como "atenuada", continuam recusadas.
- **Velocidade.** Na CPU do Colab, cada chamada leva de 30 segundos a 1,5 minuto. Para ganhar tempo sem mudar o resultado:
  - no enriquecimento, a resposta tem no máximo 150 tokens (um JSON válido usa bem menos);
  - nas respostas do assistente, o limite de 1024 tokens só trava uma resposta que não acaba;
  - o harness faz todas as perguntas da v1 e depois todas da v2, e assim o Ollama reaproveita o começo do prompt;
  - o modelo fica carregado entre as seções.

  O contexto foi fixado em 8192 tokens, para o prompt v2 com os 12 registros caber sem corte.
- **IA e regra discordando.** Vale a mais urgente das duas, e o registro vai para revisão humana. A IA pode subir a urgência (pilha no entulho), mas nunca baixar a de um ponto interditado.
- **Ponto alternativo no registro.** A IA não sabe calcular distância. Se tivesse que dizer o "ponto mais perto", inventaria. Por isso cada registro já traz o id do ponto alternativo.
- **Filtro antes da IA.** Se a pergunta cita um bairro, vão para o modelo só os pontos desse bairro e os alternativos deles. Um modelo pequeno erra menos com menos texto.
- **Prompt enxuto.** A primeira v2 tinha 662 palavras e várias frases prontas de recusa, e o modelo de 1B recusava quase tudo. A final tem os mesmos 7 elementos em cerca de 320 palavras, com uma frase de recusa só. A versão longa e o resultado de cada tentativa estão no `3_prompts_kit.md`.
- **Relato entre aspas triplas, pergunta sem aspas.** O relato do morador vai entre aspas triplas e é tratado como dado, nunca como ordem. Dois relatos têm tentativa de prompt injection de propósito. No primeiro teste, a pergunta também ia entre aspas, e o modelo tratava a própria pergunta como algo a ignorar. Por isso agora as aspas marcam só o relato.
- **Pilha e bateria são lixo perigoso.** Nenhum ponto aceita; o assistente indica o 156.
- **Sem citar a cidade.** O PDF fala de um "município médio". O assistente é da "Secretaria de Cidadania", em piloto na região da Mooca.

## Como usamos IA

- **Claude Code (Anthropic):** organizou o checklist do PDF, fez as perguntas sobre os 7 elementos do system prompt e escreveu o rascunho do código. O trio revisou, rodou e testou.
- **System prompt:** o conteúdo de cada um dos 7 elementos veio das respostas do Fidelis, uma pergunta por elemento.
- **llama3.2:1b:** classifica a urgência, reescreve os relatos e responde como assistente.
- **Notas da matriz:** dadas pelo trio. O modelo não dá nota.
- O registro completo está no `6_Chat_Log.txt`.

## O que os testes mostraram

Além do harness da Seção 5, rodamos no Colab 2 diagnósticos com as mesmas 5 perguntas, somando 90 respostas.

- **Injeção:** a v1 obedeceu ("Sim, você pode jogar pilha e bateria no entulho"); a v2 recusou.
- **Fora do escopo (T2):** a v2 recusou certo e indicou o 156.
- **O que o llama3.2:1b não conseguiu fazer**, mesmo com a regra escrita no prompt:
  - não citou o registro em nenhuma das 90 respostas;
  - não percebeu que o ponto do Tatuapé estava lotado e respondeu "Sim.";
  - não perguntou o bairro na pergunta vaga;
  - não explicou que pilha é lixo perigoso.
- **Prompt longo piora:** com a v2 longa, o modelo recusava até o que estava nos dados. A v2 enxuta seguiu melhor o exemplo no T1, mas os outros limites continuaram.

Por isso a resposta da IA nunca decide sozinha. A regra fixa da Seção 3 assume quando a IA sai do formato, e a revisão humana entra quando a IA e a regra discordam.

## Limitações

- Não tem dados em tempo real: o status vem do registro, que pode estar desatualizado.
- Os dados são simulados para o piloto; não são pontos reais.
- Só cobre 5 bairros; não funciona para outros bairros nem para outras cidades.
- Não orienta descarte de lixo perigoso ou de saúde: indica o 156.
- Não informa preço de caçamba ou frete e não atende coleta de empresa ou de obra grande.
- Não calcula distância nem considera dia da semana ou feriado.
- O llama3.2:1b é pequeno demais para seguir todas as regras do prompt: não cita o registro, não percebe ponto lotado e não pergunta o bairro quando a pergunta é vaga. Por isso há validação, regra fixa e revisão humana.
- Na CPU do Colab, o notebook inteiro leva cerca de 30 minutos; com GPU fica bem mais rápido.
