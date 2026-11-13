# Mapa dos Pontos Viciados
# GS 2026.2 - Data Structures and Algorithms - Ciclo Verde - Turma 1CCPR
# Gustavo Fidelis de Souza e Silva (RM 574666)
# Rafael Meirelles (RM 574897)
# Ana (RM 575081)
#
# Sistema de console para registrar o lixo jogado na rua na região da Mooca
# e mostrar onde ele mais volta depois de limpo.
# Sem class e sem bibliotecas: só vetores (listas), funções, busca sequencial
# e ordenação feitas à mão.


# ===================================================================
# Opções fixas
# ===================================================================

CATEGORIAS = ["Entulho de obra", "Lixo doméstico", "Móveis velhos", "Pneus",
              "Poda de árvore", "Eletrônicos", "Outros"]

BAIRROS = ["Mooca", "Água Rasa", "Belém", "Brás", "Tatuapé", "Pari"]

# A partir de 3 voltas, só limpar de novo não resolve: é um ponto viciado.
LIMITE_PONTO_VICIADO = 3


# ===================================================================
# Vetores paralelos: a posição i de todos os vetores é a mesma ocorrência
# ===================================================================

ids = []               # "OC-001", "OC-002", ...
categorias = []        # um dos nomes de CATEGORIAS
bairros = []           # um dos nomes de BAIRROS
referencias = []       # onde fica: "embaixo do viaduto", "esquina da feira"...
vezes_que_voltou = []  # quantas vezes o lixo voltou depois de limpo
dias_em_aberto = []    # há quantos dias o lixo está no lugar


def vetores_juntos():
    """Devolve os 6 vetores numa lista, sempre na mesma ordem."""
    return [ids, categorias, bairros, referencias, vezes_que_voltou, dias_em_aberto]


# ===================================================================
# Leitura e validação da entrada
# ===================================================================

def eh_numero_inteiro(texto):
    """True se o texto tem só algarismos de 0 a 9. Recusa "", "abc", "2.5" e "-1"."""
    if len(texto) == 0:
        return False
    for caractere in texto:
        if caractere < "0" or caractere > "9":
            return False
    return True


def ler_inteiro(mensagem, minimo, maximo):
    """Pede um número inteiro até a pessoa digitar um valor entre minimo e maximo."""
    while True:
        texto = input(mensagem).strip()
        if eh_numero_inteiro(texto):
            numero = int(texto)
            if numero >= minimo and numero <= maximo:
                return numero
        print(f"  Valor inválido. Digite um número inteiro de {minimo} a {maximo}.")


def ler_texto(mensagem, tamanho_maximo):
    """Pede um texto que não pode ficar vazio nem passar do tamanho máximo."""
    while True:
        texto = input(mensagem).strip()
        if len(texto) == 0:
            print("  O texto não pode ficar vazio.")
        elif len(texto) > tamanho_maximo:
            print(f"  Use no máximo {tamanho_maximo} caracteres.")
        else:
            return texto


def ler_sim_nao(mensagem):
    """Pede s ou n. Devolve True para sim e False para não."""
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta == "s" or resposta == "sim":
            return True
        if resposta == "n" or resposta == "nao" or resposta == "não":
            return False
        print("  Responda s (sim) ou n (não).")


def escolher_da_lista(titulo, opcoes):
    """Mostra as opções numeradas e devolve o nome da opção escolhida."""
    print(titulo)
    for i in range(len(opcoes)):
        print(f"  {i + 1}) {opcoes[i]}")
    numero = ler_inteiro("Número: ", 1, len(opcoes))
    return opcoes[numero - 1]


# ===================================================================
# Cadastro
# ===================================================================

def adicionar_ocorrencia(categoria, bairro, referencia, vezes, dias):
    """Coloca uma ocorrência no fim de cada vetor e devolve o id criado."""
    numero = len(ids) + 1
    novo_id = f"OC-{numero:03d}"
    ids.append(novo_id)
    categorias.append(categoria)
    bairros.append(bairro)
    referencias.append(referencia)
    vezes_que_voltou.append(vezes)
    dias_em_aberto.append(dias)
    return novo_id


def cadastrar():
    print("\n--- Cadastrar ocorrência ---")
    categoria = escolher_da_lista("Que tipo de lixo?", CATEGORIAS)
    bairro = escolher_da_lista("Em qual bairro?", BAIRROS)
    referencia = ler_texto("Onde fica? (rua, esquina ou ponto de referência): ", 60)
    vezes = ler_inteiro("Quantas vezes o lixo voltou depois de limpo? (0 a 99): ", 0, 99)
    dias = ler_inteiro("Há quantos dias o lixo está lá? (0 a 365): ", 0, 365)
    novo_id = adicionar_ocorrencia(categoria, bairro, referencia, vezes, dias)
    print(f"Ocorrência {novo_id} cadastrada.")
    avisar_ponto_viciado(bairro, referencia, vezes)


def contar_no_mesmo_local(bairro, referencia):
    """Busca sequencial no bairro e conta os registros com o mesmo local (sem ligar para maiúsculas)."""
    contador = 0
    for i in busca_sequencial(bairros, bairro):
        if referencias[i].lower() == referencia.lower():
            contador = contador + 1
    return contador


def avisar_ponto_viciado(bairro, referencia, vezes):
    """Alerta quando o local já tem 3 registros ou mais, ou quando o lixo já voltou 3 vezes ou mais."""
    no_mesmo_local = contar_no_mesmo_local(bairro, referencia)
    if no_mesmo_local >= LIMITE_PONTO_VICIADO or vezes >= LIMITE_PONTO_VICIADO:
        print("ATENÇÃO: ponto viciado. Precisa de ação além da limpeza (placa, câmera, ecoponto perto).")
        if no_mesmo_local >= LIMITE_PONTO_VICIADO:
            print(f"  Motivo: o local já tem {no_mesmo_local} registros.")
        if vezes >= LIMITE_PONTO_VICIADO:
            print(f"  Motivo: o lixo já voltou {vezes} vezes depois de limpo.")


def carregar_exemplos():
    """18 ocorrências simuladas, para a demonstração não começar vazia."""
    adicionar_ocorrencia("Entulho de obra", "Brás", "embaixo do viaduto", 6, 40)
    adicionar_ocorrencia("Lixo doméstico", "Mooca", "esquina perto da feira de domingo", 4, 12)
    adicionar_ocorrencia("Móveis velhos", "Belém", "calçada em frente ao terreno vazio", 2, 20)
    adicionar_ocorrencia("Pneus", "Tatuapé", "beira do córrego", 3, 35)
    adicionar_ocorrencia("Entulho de obra", "Mooca", "rua sem saída atrás da escola", 5, 28)
    adicionar_ocorrencia("Poda de árvore", "Água Rasa", "praça do bairro", 0, 5)
    adicionar_ocorrencia("Lixo doméstico", "Brás", "perto da estação de trem", 7, 9)
    adicionar_ocorrencia("Eletrônicos", "Pari", "ao lado do ponto de ônibus", 1, 15)
    adicionar_ocorrencia("Entulho de obra", "Belém", "terreno vazio da esquina", 3, 50)
    adicionar_ocorrencia("Móveis velhos", "Brás", "embaixo do viaduto", 4, 18)
    adicionar_ocorrencia("Lixo doméstico", "Tatuapé", "atrás do mercado", 2, 7)
    adicionar_ocorrencia("Outros", "Mooca", "muro da linha do trem", 1, 3)
    adicionar_ocorrencia("Entulho de obra", "Água Rasa", "rua da padaria", 6, 22)
    adicionar_ocorrencia("Pneus", "Brás", "galpão abandonado", 3, 60)
    adicionar_ocorrencia("Móveis velhos", "Mooca", "esquina perto da feira de domingo", 0, 2)
    adicionar_ocorrencia("Poda de árvore", "Belém", "canteiro da avenida", 1, 10)
    adicionar_ocorrencia("Lixo doméstico", "Brás", "saída da rua comercial", 5, 14)
    adicionar_ocorrencia("Entulho de obra", "Tatuapé", "beira do córrego", 2, 33)


# ===================================================================
# Mostrar na tela
# ===================================================================

def cortar(texto, tamanho):
    """Corta textos longos para caber na coluna da tabela."""
    if len(texto) <= tamanho:
        return texto
    return texto[:tamanho - 3] + "..."


def formatar_decimal(valor):
    """1 casa decimal, com vírgula: 12.5 vira "12,5"."""
    return f"{valor:.1f}".replace(".", ",")


def todas_as_posicoes(quantidade):
    """Devolve [0, 1, 2, ..., quantidade - 1]."""
    posicoes = []
    for i in range(quantidade):
        posicoes.append(i)
    return posicoes


def mostrar_tabela(juntos, posicoes, numerar):
    """Mostra as ocorrências das posições pedidas. Se numerar for True, mostra a colocação."""
    v_ids, v_categorias, v_bairros, v_referencias, v_vezes, v_dias = juntos
    print(f"{'#':>3}  {'ID':<6}  {'Tipo de lixo':<15}  {'Bairro':<9}  {'Onde fica':<32}  {'Voltou':>6}  {'Dias':>4}")
    print("-" * 87)
    colocacao = 0
    for i in posicoes:
        colocacao = colocacao + 1
        if numerar:
            numero = f"{colocacao}º"
        else:
            numero = ""
        print(f"{numero:>3}  {v_ids[i]:<6}  {v_categorias[i]:<15}  {v_bairros[i]:<9}  "
              f"{cortar(v_referencias[i], 32):<32}  {v_vezes[i]:>6}  {v_dias[i]:>4}")


def listar():
    print("\n--- Todas as ocorrências ---")
    if len(ids) == 0:
        print("Nenhuma ocorrência cadastrada.")
        return
    mostrar_tabela(vetores_juntos(), todas_as_posicoes(len(ids)), False)
    print(f"Total: {len(ids)} ocorrência(s).")


# ===================================================================
# Busca sequencial
# ===================================================================

def busca_sequencial(vetor, valor):
    """Percorre o vetor do começo ao fim e guarda cada posição onde achou o valor."""
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == valor:
            posicoes.append(i)
    return posicoes


def mostrar_resultado_busca(posicoes, descricao):
    if len(posicoes) == 0:
        print(f"Nenhuma ocorrência {descricao}.")
        return
    mostrar_tabela(vetores_juntos(), posicoes, False)
    print(f"{len(posicoes)} ocorrência(s) {descricao}.")


def buscar_por_categoria():
    print("\n--- Buscar por tipo de lixo ---")
    if len(ids) == 0:
        print("Nenhuma ocorrência cadastrada.")
        return
    categoria = escolher_da_lista("Qual tipo de lixo?", CATEGORIAS)
    posicoes = busca_sequencial(categorias, categoria)
    mostrar_resultado_busca(posicoes, f"de {categoria}")


def buscar_por_bairro():
    print("\n--- Buscar por bairro ---")
    if len(ids) == 0:
        print("Nenhuma ocorrência cadastrada.")
        return
    bairro = escolher_da_lista("Qual bairro?", BAIRROS)
    posicoes = busca_sequencial(bairros, bairro)
    mostrar_resultado_busca(posicoes, f"em {bairro}")


# ===================================================================
# Ordenação por seleção
# ===================================================================

def copiar_vetor(vetor):
    copia = []
    for valor in vetor:
        copia.append(valor)
    return copia


def copiar_todos():
    """Copia os 6 vetores. Assim a ordenação não muda a ordem do cadastro."""
    copias = []
    for vetor in vetores_juntos():
        copias.append(copiar_vetor(vetor))
    return copias


def trocar(juntos, i, j):
    """Troca as posições i e j em TODOS os vetores, para a ocorrência não se misturar."""
    for vetor in juntos:
        auxiliar = vetor[i]
        vetor[i] = vetor[j]
        vetor[j] = auxiliar


def vem_antes(v_vezes, v_dias, v_ids, a, b, criterio):
    """True se a ocorrência da posição a deve aparecer antes da posição b."""
    if criterio == "reincidencia":
        if v_vezes[a] != v_vezes[b]:
            return v_vezes[a] > v_vezes[b]
        if v_dias[a] != v_dias[b]:
            return v_dias[a] > v_dias[b]
    else:  # criterio == "dias"
        if v_dias[a] != v_dias[b]:
            return v_dias[a] > v_dias[b]
        if v_vezes[a] != v_vezes[b]:
            return v_vezes[a] > v_vezes[b]
    # Empate nos dois números: o cadastro mais antigo vem primeiro.
    return v_ids[a] < v_ids[b]


def ordenar_por_selecao(criterio):
    """Ordenação por seleção, em cópias dos vetores.

    A cada passada, procura a ocorrência que deve vir primeiro entre as que
    sobraram e a troca com a posição da vez. Devolve as cópias ordenadas e o
    número de comparações feitas.
    """
    juntos = copiar_todos()
    v_ids, v_categorias, v_bairros, v_referencias, v_vezes, v_dias = juntos
    quantidade = len(v_ids)
    comparacoes = 0
    for i in range(quantidade - 1):
        escolhida = i
        for j in range(i + 1, quantidade):
            comparacoes = comparacoes + 1
            if vem_antes(v_vezes, v_dias, v_ids, j, escolhida, criterio):
                escolhida = j
        if escolhida != i:
            trocar(juntos, i, escolhida)
    return juntos, comparacoes


def ordenar_por_bolha(criterio):
    """Ordenação por bolha (bubble sort), em cópias dos vetores, para comparar com a seleção.

    Compara vizinhos e troca os que estão fora de ordem. Se uma passada
    inteira não troca nada, a lista já está ordenada e o laço para antes.
    """
    juntos = copiar_todos()
    v_ids, v_categorias, v_bairros, v_referencias, v_vezes, v_dias = juntos
    quantidade = len(v_ids)
    comparacoes = 0
    for passada in range(quantidade - 1):
        trocou = False
        for j in range(quantidade - 1 - passada):
            comparacoes = comparacoes + 1
            if vem_antes(v_vezes, v_dias, v_ids, j + 1, j, criterio):
                trocar(juntos, j, j + 1)
                trocou = True
        if not trocou:
            break
    return juntos, comparacoes


def comparar_ordenacoes():
    print("\n--- Comparar seleção e bolha ---")
    quantidade = len(ids)
    if quantidade < 2:
        print("São precisas pelo menos 2 ocorrências para comparar.")
        return
    selecao, comparacoes_selecao = ordenar_por_selecao("reincidencia")
    bolha, comparacoes_bolha = ordenar_por_bolha("reincidencia")
    mesma_ordem = True
    for i in range(quantidade):
        if selecao[0][i] != bolha[0][i]:  # o vetor 0 é o dos ids
            mesma_ordem = False
    print(f"Ocorrências ordenadas por reincidência: {quantidade}")
    print(f"  Seleção: {comparacoes_selecao} comparações")
    print(f"  Bolha:   {comparacoes_bolha} comparações")
    if mesma_ordem:
        print("As duas chegaram à mesma ordem.")
    else:
        print("ERRO: as duas ordens ficaram diferentes.")
    print("A seleção faz sempre o mesmo número de comparações. A bolha para antes quando")
    print("uma passada não troca nada, então depende de como os dados já estão.")


def mostrar_ranking():
    print("\n--- Ranking dos pontos viciados ---")
    if len(ids) == 0:
        print("Nenhuma ocorrência cadastrada.")
        return
    print("Ordenar por:")
    print("  1) Reincidência: onde o lixo mais volta (empate: mais dias em aberto)")
    print("  2) Dias em aberto: lixo parado há mais tempo (empate: mais reincidência)")
    escolha = ler_inteiro("Número: ", 1, 2)
    if escolha == 1:
        criterio = "reincidencia"
    else:
        criterio = "dias"
    juntos, comparacoes = ordenar_por_selecao(criterio)
    mostrar_tabela(juntos, todas_as_posicoes(len(ids)), True)
    print(f"Ordenado com o algoritmo de seleção: {comparacoes} comparações.")
    print(f"Pontos que voltaram {LIMITE_PONTO_VICIADO} vezes ou mais precisam de ação além da limpeza "
          f"(placa, câmera, ecoponto perto).")


# ===================================================================
# Estatísticas: contadores e acumuladores
# ===================================================================

def contar_por_opcao(opcoes, vetor):
    """Para cada opção, conta quantas vezes ela aparece no vetor."""
    contagens = []
    for opcao in opcoes:
        contador = 0
        for valor in vetor:
            if valor == opcao:
                contador = contador + 1
        contagens.append(contador)
    return contagens


def maiores(opcoes, contagens):
    """Acha o maior número e devolve os nomes que têm esse número (pode haver empate)."""
    maior = contagens[0]
    for contagem in contagens:
        if contagem > maior:
            maior = contagem
    nomes = []
    for i in range(len(opcoes)):
        if contagens[i] == maior:
            nomes.append(opcoes[i])
    return nomes, maior


def mostrar_barras(opcoes, contagens, total):
    for i in range(len(opcoes)):
        barra = "#" * contagens[i]
        percentual = contagens[i] * 100 / total
        print(f"  {opcoes[i]:<15}  {barra:<10}  {contagens[i]:>2}  ({formatar_decimal(percentual)}%)")


def mostrar_estatisticas():
    print("\n--- Estatísticas ---")
    total = len(ids)
    if total == 0:
        print("Nenhuma ocorrência cadastrada. Cadastre uma antes de ver as estatísticas.")
        return

    soma_dias = 0          # acumulador
    soma_voltas = 0        # acumulador
    pontos_viciados = 0    # contador
    for i in range(total):
        soma_dias = soma_dias + dias_em_aberto[i]
        soma_voltas = soma_voltas + vezes_que_voltou[i]
        if vezes_que_voltou[i] >= LIMITE_PONTO_VICIADO:
            pontos_viciados = pontos_viciados + 1

    por_categoria = contar_por_opcao(CATEGORIAS, categorias)
    por_bairro = contar_por_opcao(BAIRROS, bairros)

    print(f"Total de ocorrências: {total}")
    print(f"Média de dias com o lixo no lugar: {formatar_decimal(soma_dias / total)} dias")
    print(f"Vezes que o lixo voltou depois de limpo: {soma_voltas} no total "
          f"(média de {formatar_decimal(soma_voltas / total)} por ponto)")
    print(f"Pontos viciados (voltou {LIMITE_PONTO_VICIADO} vezes ou mais): {pontos_viciados} de {total}")

    print("\nPor tipo de lixo:")
    mostrar_barras(CATEGORIAS, por_categoria, total)
    print("\nPor bairro:")
    mostrar_barras(BAIRROS, por_bairro, total)

    nomes, maior = maiores(BAIRROS, por_bairro)
    print(f"\nBairro com mais ocorrências: {', '.join(nomes)} ({maior})")
    nomes, maior = maiores(CATEGORIAS, por_categoria)
    print(f"Tipo de lixo mais comum: {', '.join(nomes)} ({maior})")


# ===================================================================
# Menu principal
# ===================================================================

def mostrar_menu():
    print("\n========== MAPA DOS PONTOS VICIADOS ==========")
    print("1) Cadastrar ocorrência")
    print("2) Listar todas")
    print("3) Buscar por tipo de lixo")
    print("4) Buscar por bairro")
    print("5) Ranking dos pontos viciados")
    print("6) Estatísticas")
    print("7) Comparar seleção e bolha")
    print("0) Sair")


def principal():
    print("Mapa dos Pontos Viciados - Ciclo Verde")
    print("Registre o lixo jogado na rua e veja onde ele mais volta.")
    if ler_sim_nao("Carregar as ocorrências de exemplo (dados simulados)? (s/n): "):
        carregar_exemplos()
        print(f"{len(ids)} ocorrências de exemplo carregadas.")
    else:
        print("Começando sem nenhuma ocorrência.")

    while True:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opção: ", 0, 7)
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            buscar_por_categoria()
        elif opcao == 4:
            buscar_por_bairro()
        elif opcao == 5:
            mostrar_ranking()
        elif opcao == 6:
            mostrar_estatisticas()
        elif opcao == 7:
            comparar_ordenacoes()
        else:
            print("Até logo! Descarte certo deixa a rua limpa.")
            break


if __name__ == "__main__":
    try:
        principal()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma encerrado.")
