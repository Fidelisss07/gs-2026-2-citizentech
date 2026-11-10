# 07 — Prompt and AI: assistente de serviços públicos essenciais da Mooca (frente D)

Responsável: Gustavo Fidelis. Entrega: ZIP com 6 arquivos de nome fixo.

## Andamento

| Seção do notebook | Situação |
| --- | --- |
| 0. Metadados | Rascunho (falta modalidade, RM da Ana, divisão de tarefas e declaração de IA com as palavras do grupo) |
| 1. Coleta e estruturação dos dados | Pronta: 15 registros brutos, 13 aprovados, 4 com status fora do normal, 4 regras aplicadas, gera `2_dados_servico.json` |
| 2. Enriquecimento com LLM | Pronta (falta rodar no Colab com a chave): urgência + resumo de 140 caracteres, respostas guardadas em lista, tabela relato × resumo |
| 3. Validação e governança | Pronta: 5 verificações, fallback por status, coluna `fonte`, regra → IA → humano (vale a mais grave), trilha com versão do prompt e horário |
| 4 a 7 | Em construção |

## Como rodar

1. Abrir `1_Notebook_GS2026_2.ipynb` no Google Colab.
2. Em Secrets (ícone de chave), criar `OLLAMA_API_KEY` com a sua chave. **Nunca** colar a chave no código.
3. Runtime → Run all. O arquivo `2_dados_servico.json` é gerado pelo próprio notebook.
