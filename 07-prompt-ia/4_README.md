# Ciclo Verde: assistente de descarte da região da Mooca

**GS 2026.2 · Prompt and Artificial Intelligence · Prof. Jorge Luiz Gomes**
**Turma 1CCPR · Trio · Frente B: Descarte e sustentabilidade**

| Integrante | RM |
| --- | --- |
| Gustavo Fidelis de Souza e Silva | 574666 |
| Rafael Meirelles | 574897 |
| Ana | a confirmar |

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
2. No ícone de chave (Secrets), na barra da esquerda, crie o segredo `OLLAMA_API_KEY` com a sua chave do Ollama Cloud e ligue o "Acesso ao notebook".
3. Clique em **Ambiente de execução → Executar tudo** (Runtime → Run all).
4. O notebook grava o `2_dados_servico.json` na pasta do Colab (ícone de pasta). Baixe o arquivo.

Não usa nenhuma API paga. A chave nunca aparece no notebook: ela é lida com `userdata.get('OLLAMA_API_KEY')`.

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
- **Dados simulados com erros de propósito.** Os dados brutos têm `acessivel` escrito como texto, horários em formatos diferentes, um ponto lotado sem motivo e um id repetido. Assim as 4 regras de negócio têm o que corrigir, e o notebook mostra quantas correções fez.
- **Onde ficam as 4 regras.** O PDF fala da Seção 3 num lugar e da Seção 1 em outro. Aplicamos as regras na Seção 1, antes de gravar o JSON, e conferimos de novo na Seção 3, relendo o arquivo gravado.
- **Regra 1.** O texto da regra 1 no PDF diz o contrário da tabela do esquema. Seguimos a tabela: status diferente de `ativo` precisa de motivo.
- **Horário.** "24h" não é uma hora e "08:00" é texto. Por isso todo horário vira um formato só e a função `esta_aberto()` compara em minutos. Nos testes a hora da consulta é fixa (10:00), para o resultado poder ser repetido.
- **Temperatura 0.1.** Para classificar e responder, queremos a mesma saída para a mesma entrada, e não criatividade.
- **Validação e regra fixa.** A resposta da IA só vale se a urgência for `urgente`, `atencao` ou `ok`, nenhum campo vier vazio e o resumo tiver até 140 caracteres. Se falhar, a regra fixa decide.
- **IA e regra discordando.** Vale a mais urgente das duas, e o registro vai para revisão humana. A IA pode subir a urgência (pilha no entulho), mas nunca baixar a de um ponto interditado.
- **Ponto alternativo no registro.** A IA não sabe calcular distância. Se tivesse que dizer o "ponto mais perto", inventaria. Por isso cada registro já traz o id do ponto alternativo.
- **Filtro antes da IA.** Se a pergunta cita um bairro, vão para o modelo só os pontos desse bairro e os alternativos deles. Um modelo pequeno erra menos com menos texto.
- **Relato e pergunta entre aspas triplas.** O relato do morador é tratado como dado, nunca como ordem. Dois relatos têm tentativa de prompt injection de propósito.
- **Pilha e bateria são lixo perigoso.** Nenhum ponto aceita; o assistente indica o 156.
- **Sem citar a cidade.** O PDF fala de um "município médio". O assistente é da "Secretaria de Cidadania", em piloto na região da Mooca.

## Como usamos IA

- **Claude Code (Anthropic):** organizou o checklist do PDF, fez as perguntas sobre os 7 elementos do system prompt e escreveu o rascunho do código. O trio revisou, rodou e testou.
- **System prompt:** o conteúdo de cada um dos 7 elementos veio das respostas do Fidelis, uma pergunta por elemento.
- **llama3.2:1b:** classifica a urgência, reescreve os relatos e responde como assistente.
- **Notas da matriz:** dadas pelo trio. O modelo não dá nota.
- O registro completo está no `6_Chat_Log.txt`.

## Limitações

- Não tem dados em tempo real: o status vem do registro, que pode estar desatualizado.
- Os dados são simulados para o piloto; não são pontos reais.
- Só cobre 5 bairros; não funciona para outros bairros nem para outras cidades.
- Não orienta descarte de lixo perigoso ou de saúde: indica o 156.
- Não informa preço de caçamba ou frete e não atende coleta de empresa ou de obra grande.
- Não calcula distância nem considera dia da semana ou feriado.
- O llama3.2:1b é pequeno e pode errar em perguntas longas; por isso há validação e regra fixa.
