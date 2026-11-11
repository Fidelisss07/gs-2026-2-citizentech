# 07 — Prompt and AI: assistente de serviços públicos essenciais da Mooca (frente D)

Responsável: Gustavo Fidelis. Entrega: ZIP com 6 arquivos de nome fixo.

## Andamento

| Seção do notebook | Situação |
| --- | --- |
| 0. Metadados | Rascunho (falta modalidade, RM da Ana, divisão de tarefas e declaração de IA com as palavras do grupo) |
| 1. Coleta e estruturação dos dados | Pronta: 15 registros brutos, 13 aprovados, 4 com status fora do normal, 4 regras aplicadas, gera `2_dados_servico.json` |
| 2. Enriquecimento com LLM | Pronta (falta rodar no Colab com a chave): urgência + resumo de 140 caracteres, respostas guardadas em lista, tabela relato × resumo |
| 3. Validação e governança | Pronta: 5 verificações, fallback por status, coluna `fonte`, regra → IA → humano (vale a mais grave), trilha com versão do prompt e horário |
| 4. Construção do system prompt | Pronta: v1, v2 (7 elementos) e final; prompt impresso em markdown; mapa elemento → trecho |
| 5. Testes e avaliação | Pronta: 5 perguntas × v1/v2, verificações automáticas, consistência (3 rodadas), ataque e defesa (5 ataques). **Falta: notas humanas e texto da melhora v1 → v2** |
| 6. Uso e limites da solução | Pronta: bloco JSON + 8 limitações + prévia do app Mooca Já (extra) |
| 7. Conclusão | Rascunho (reescrever com as palavras do grupo) + tela final que grava `5_certificacao.txt` |

## Arquivos da entrega

| Arquivo | Situação |
| --- | --- |
| `1_Notebook_GS2026_2.ipynb` | Pronto para rodar no Colab |
| `2_dados_servico.json` | Gerado pelo notebook |
| `3_prompts_kit.md` | Pronto (falta o resultado das iterações após rodar) |
| `4_README.md` | A fazer (precisa dos prints do Colab) |
| `5_certificacao.txt` | Gerado pela última célula do notebook |
| `6_Chat_Log.txt` | Rascunho pronto (atualizar no fim) |

## Como rodar

1. Abrir `1_Notebook_GS2026_2.ipynb` no Google Colab.
2. Em Secrets (ícone de chave), criar `OLLAMA_API_KEY` com a sua chave. **Nunca** colar a chave no código.
3. Runtime → Run all. O arquivo `2_dados_servico.json` é gerado pelo próprio notebook.

## Modelo

O `llama3.2:1b` não está no catálogo do Ollama Cloud. A Seção 1 tenta o Cloud e, se não der, instala o Ollama
dentro do Colab e baixa o modelo (grátis, ~2 minutos). Confirmar com o Prof. Jorge se isso está ok.
