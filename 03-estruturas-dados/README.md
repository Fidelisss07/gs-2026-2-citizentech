# Mapa dos Pontos Viciados

**GS 2026.2 · Data Structures and Algorithms · Turma 1CCPR · Trio Ciclo Verde**

| Integrante | RM |
| --- | --- |
| Gustavo Fidelis de Souza e Silva | 574666 |
| Rafael Meirelles | 574897 |
| Anna Luisa Lima | 575081 |

## O que é

Um sistema de console, em Python, para registrar o lixo jogado na rua na região da Mooca (Mooca, Água Rasa, Belém, Brás, Tatuapé e Pari) e mostrar onde ele mais volta depois de limpo. Esses lugares são os "pontos viciados".

O PDF da disciplina dá como exemplos "buraco, iluminação, lixo, enchente, entre outros". O trio escolheu um desses problemas, o descarte irregular de lixo, e aprofundou nele. Por isso as categorias do sistema são tipos de lixo.

## Como rodar

Precisa só do Python 3 (testado no 3.14). Não precisa instalar nada.

```
python mapa_pontos_viciados.py
```

Ao abrir, o sistema pergunta se deve carregar 18 ocorrências de exemplo. Elas são **dados simulados**, não registros reais. Responda `s` para ver o sistema com dados, ou `n` para começar vazio.

## O que o sistema faz

| Opção | O que faz |
| --- | --- |
| 1) Cadastrar ocorrência | Tipo de lixo e bairro (escolhidos por número), local, quantas vezes o lixo voltou depois de limpo e há quantos dias está lá. Avisa quando o lugar é um ponto viciado e diz o motivo |
| 2) Listar todas | Tabela com todas as ocorrências, na ordem do cadastro |
| 3) Buscar por tipo de lixo | Busca sequencial no vetor de categorias |
| 4) Buscar por bairro | Busca sequencial no vetor de bairros |
| 5) Ranking dos pontos viciados | Ordenação por seleção, por reincidência ou por dias em aberto |
| 6) Estatísticas | Total, média de dias, soma e média das voltas, pontos viciados, contagem por tipo e por bairro, bairro e tipo mais comuns |
| 7) Comparar seleção e bolha | Ordena com os dois algoritmos e mostra quantas comparações cada um fez |
| 0) Sair | Encerra o programa |

Entrada errada não quebra o programa: letra no lugar de número, opção fora da lista, texto vazio ou longo demais e número negativo são recusados com uma mensagem, e o sistema pergunta de novo. Com a lista vazia, as opções 2 a 7 avisam que não há ocorrências.

## Onde está cada conteúdo da disciplina

| Conteúdo | Onde está no código |
| --- | --- |
| Variáveis e tipos de dados | `str` (ids, tipos, bairros, locais), `int` (voltas, dias, contadores), `float` (médias), `bool` (`trocou`, `mesma_ordem`, resposta de `ler_sim_nao`) |
| Estruturas de decisão | `if`/`elif`/`else` no menu (`principal`), na comparação do ranking (`vem_antes`) e nas validações |
| Estruturas de repetição | `while True` no menu e nas leituras (`ler_inteiro`, `ler_texto`); `for` nas buscas, ordenações e estatísticas |
| Funções | 34 funções, uma para cada tarefa |
| Vetores | 6 vetores paralelos: `ids`, `categorias`, `bairros`, `referencias`, `vezes_que_voltou`, `dias_em_aberto` |
| Busca sequencial | `busca_sequencial`, usada por `buscar_por_categoria`, `buscar_por_bairro` e `contar_no_mesmo_local` |
| Ordenação | `ordenar_por_selecao` (ranking) e `ordenar_por_bolha` (para comparar). Sem `sort()` nem `sorted()` |
| Contadores | `contar_por_opcao`, `pontos_viciados`, `comparacoes` |
| Acumuladores | `soma_dias` e `soma_voltas` em `mostrar_estatisticas` |

O código não usa `class` nem nenhum `import`.

## Decisões

- **Vetores paralelos.** A posição `i` de todos os vetores é a mesma ocorrência. A ordenação trabalha em cópias e troca as posições nos 6 vetores juntos, para os dados de uma ocorrência não se misturarem com os de outra. A ordem do cadastro não muda.
- **Critérios de ordenação.** Por reincidência (onde o lixo mais volta; no empate, mais dias em aberto) ou por dias em aberto (no empate, mais reincidência). Um ponto onde o lixo voltou 5 vezes precisa de outra ação (placa, câmera, ecoponto perto), não só de mais uma limpeza.
- **Ponto viciado = 3 ou mais.** O alerta do cadastro aparece quando o local já tem 3 registros ou quando o lixo já voltou 3 vezes, e diz qual dos motivos disparou.
- **Tipo de lixo e bairro escolhidos por número.** Assim não tem erro de digitação nem de acento, e a busca sempre encontra.
- **Dados só na memória.** O PDF não pede que o sistema grave os dados em arquivo.

## Testes

Rodamos o sistema com roteiros de entrada:
- o fluxo normal;
- as entradas erradas (letra, opção inválida, texto vazio, texto longo, número negativo);
- a lista vazia;
- o alerta com os dois motivos;
- a comparação dos algoritmos;
- a entrada que acaba no meio.

Nenhum roteiro deu erro. Com os 18 exemplos, a seleção fez 153 comparações (18 × 17 ÷ 2) e a bolha fez 143.

## Arquivos

| Arquivo | O que é |
| --- | --- |
| `mapa_pontos_viciados.py` | O sistema |
| `diagrama_atividades.png` | Diagrama de atividades (UML) |
| `diagrama_atividades.mmd` | O texto do diagrama, em Mermaid, para editar |
| `relatorio.md` | Texto do relatório técnico |
| `relatorio_tecnico.pdf` | Relatório técnico em PDF (entrega) |
| `link_video.txt` | Nomes, RMs e o link do vídeo |
| `video/demonstracao_mapa_pontos_viciados.mp4` | Vídeo de demonstração (2min40) |

## Vídeo

Vídeo de demonstração (2min40): [`video/demonstracao_mapa_pontos_viciados.mp4`](video/demonstracao_mapa_pontos_viciados.mp4)

O vídeo mostra o programa rodando com os dados de exemplo, ao lado de uma animação dos vetores, da busca e da ordenação. A animação foi feita com o Claude Code, e a narração usa uma voz de IA (ElevenLabs).

## O que cada um fez

| Integrante | O que fez |
| --- | --- |
| Gustavo Fidelis de Souza e Silva | Definiu as decisões do projeto, conferiu o código e os testes e revisou o vídeo |
| Rafael Meirelles | [a preencher] |
| Anna Luisa Lima | Escreveu os benefícios para a comunidade (seção 8 do relatório) |

## Uso de IA

- **Claude Code (Anthropic):** montou o checklist do PDF e escreveu o rascunho do código, dos roteiros de teste, do diagrama e do relatório.
- **Decisões do projeto:** foram aprovadas pelo Fidelis, que conferiu o checklist e os testes com a ajuda do Claude (chat). São elas: as categorias, os vetores paralelos, os critérios de ordenação, os dois motivos do alerta e o "0" para sair.
