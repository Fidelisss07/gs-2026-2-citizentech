# Diario de Descarte da Casa - Ciclo Verde
# Global Solution 2026.2 - Pensamento Computacional e Automacao em Python - Turma 1CCPR
# Gustavo Fidelis de Souza e Silva (RM 574666) | Rafael Meirelles (RM 574897) | Anna Luisa Lima (RM 575081)
#
# INTRODUCAO
# Problema: na Mooca, o lixo jogado na rua volta sempre aos mesmos "pontos viciados", e o
#   lixo organico vai para o aterro em vez de virar adubo.
# Publico: moradores da regiao que querem descartar o lixo de casa do jeito certo.
# Objetivo: registrar cada descarte, dizer se foi certo ou errado, calcular indicadores
#   da casa e dar uma recomendacao automatica.
# ODS: 11 (cidades sustentaveis), 12 (consumo responsavel) e 13 (acao climatica).


# ---------- listas fixas: tipos de lixo e destinos ----------
# A posicao na lista + 1 e o numero que aparece no menu.

TIPOS = [
    "Organico",       # 1
    "Reciclavel",     # 2
    "Oleo de cozinha",  # 3
    "Eletronico",     # 4
    "Pilha/bateria",  # 5
    "Entulho",        # 6
    "Movel velho",    # 7
    "Rejeito",        # 8 (fralda, papel higienico, bituca)
]

DESTINOS = [
    "Compostagem",        # 1
    "Coleta seletiva",    # 2
    "Ecoponto",           # 3
    "Ponto de entrega",   # 4 (mercados e lojas: pilha, oleo, eletronico)
    "Coleta comum",       # 5
    "Rua/terreno",        # 6
]

# Dica para cada tipo, na mesma ordem da lista TIPOS
DICAS = [
    "Organico vira adubo: leve ao ponto de compostagem da horta.",
    "Separe o reciclavel para a coleta seletiva ou leve ao ecoponto.",
    "Guarde o oleo frio em recipiente fechado e confirme um ponto que o aceite.",
    "Leve o eletronico a um ponto que confirme receber esse material.",
    "Pilha e bateria sao lixo perigoso: so em ponto de entrega (mercados e lojas).",
    "Entulho vai ao ecoponto, de graca. Na rua ele cria ponto viciado.",
    "Consulte um ecoponto ou o servico municipal para destinar moveis velhos.",
    "Rejeito nao recicla: vai no saco da coleta comum, nunca na rua.",
]

# ---------- listas dos registros ----------
# Cada descarte ocupa a mesma posicao nas quatro listas.
tipos_reg = []      # numero do tipo (1 a 8)
destinos_reg = []   # numero do destino (1 a 6)
pesos_reg = []      # peso em kg
certos_reg = []     # True = descarte certo, False = descarte errado


# ---------- funcoes de entrada (com validacao) ----------

def ler_inteiro(mensagem, minimo, maximo):
    """Pede um numero inteiro entre minimo e maximo ate o usuario acertar."""
    while True:
        texto = input(mensagem).strip()
        if not texto.isascii() or not texto.isdecimal() or len(texto) > 12:
            print(f"  Digite um numero de {minimo} a {maximo}.")
        elif int(texto) < minimo or int(texto) > maximo:
            print(f"  Opcao invalida. Escolha de {minimo} a {maximo}.")
        else:
            return int(texto)


def ler_peso():
    """Pede o peso em kg (aceita virgula ou ponto). Precisa ser maior que zero."""
    while True:
        texto = input("Peso aproximado em kg: ").strip().replace(",", ".")
        try:
            peso = float(texto)
        except ValueError:
            print("  Digite um numero, por exemplo 1.5")
            continue
        if peso > 0 and peso <= 1000:
            return peso
        print("  O peso precisa ser maior que 0 e no maximo 1000 kg.")


def mostrar_opcoes(lista, titulo):
    """Mostra uma lista numerada e devolve o numero escolhido."""
    print("\n" + titulo)
    for i in range(len(lista)):
        print(f"  {i + 1} - {lista[i]}")
    return ler_inteiro("Escolha: ", 1, len(lista))


# ---------- classificacao (if/elif/else) ----------

def classificar(tipo, destino):
    """Devolve True se o descarte foi certo e False se foi errado.

    Destinos: 1 compostagem, 2 coleta seletiva, 3 ecoponto,
              4 ponto de entrega, 5 coleta comum, 6 rua.
    """
    if destino == 6:                      # rua ou terreno: sempre errado
        return False
    elif tipo == 1:                       # organico
        return destino == 1
    elif tipo == 2:                       # reciclavel
        return destino == 2 or destino == 3
    elif tipo == 3 or tipo == 4:          # oleo ou eletronico
        return destino == 3 or destino == 4
    elif tipo == 5:                       # pilha ou bateria
        return destino == 4
    elif tipo == 6 or tipo == 7:          # entulho ou movel
        return destino == 3
    else:                                 # rejeito
        return destino == 5


def nivel(percentual):
    """Classifica a casa pelo percentual de descarte certo."""
    if percentual >= 80:
        return "OTIMO"
    elif percentual >= 50:
        return "REGULAR"
    else:
        return "PRECISA MELHORAR"


# ---------- opcoes do menu ----------

def cadastrar():
    tipo = mostrar_opcoes(TIPOS, "Que tipo de lixo foi descartado?")
    destino = mostrar_opcoes(DESTINOS, "Para onde ele foi?")
    peso = ler_peso()
    certo = classificar(tipo, destino)

    tipos_reg.append(tipo)
    destinos_reg.append(destino)
    pesos_reg.append(peso)
    certos_reg.append(certo)

    if certo:
        print("\n  DESCARTE CERTO! Obrigado por cuidar do bairro.")
    else:
        print("\n  DESCARTE ERRADO.")
        print("  Dica: " + DICAS[tipo - 1])


def listar():
    if len(tipos_reg) == 0:
        print("\nNenhum descarte cadastrado ainda.")
        return
    print(f"\n{'N':>3}  {'Tipo':<16} {'Destino':<17} {'Peso':>8}  Resultado")
    for i in range(len(tipos_reg)):
        if certos_reg[i]:
            resultado = "certo"
        else:
            resultado = "ERRADO"
        tipo = TIPOS[tipos_reg[i] - 1]
        destino = DESTINOS[destinos_reg[i] - 1]
        print(f"{i + 1:>3}  {tipo:<16} {destino:<17} {pesos_reg[i]:>6.1f}kg  {resultado}")


def calcular_indicadores():
    """Percorre as listas e devolve os indicadores numa lista:
    [total, certo_kg, percentual, organico, adubo, na_rua, mais_comum, pior_tipo]
    """
    total = 0
    certo_kg = 0
    organico = 0          # todo o organico (o que PODERIA virar adubo)
    adubo = 0             # organico que FOI para a compostagem; massa de adubo nao e medida
    na_rua = 0
    kg_por_tipo = [0] * len(TIPOS)       # soma de kg de cada tipo
    errado_por_tipo = [0] * len(TIPOS)   # soma de kg descartado errado de cada tipo

    for i in range(len(tipos_reg)):
        tipo = tipos_reg[i]
        peso = pesos_reg[i]
        total += peso
        kg_por_tipo[tipo - 1] += peso
        if tipo == 1:
            organico += peso
        if certos_reg[i]:
            certo_kg += peso
            if tipo == 1:
                adubo += peso
        else:
            errado_por_tipo[tipo - 1] += peso
        if destinos_reg[i] == 6:
            na_rua += peso

    percentual = certo_kg / total * 100 if total > 0 else 0

    # tipo com mais kg (maior valor da lista)
    mais_comum = 0
    for t in range(len(TIPOS)):
        if kg_por_tipo[t] > kg_por_tipo[mais_comum]:
            mais_comum = t

    # tipo com mais kg descartado errado (-1 = nenhum)
    pior_tipo = -1
    maior_erro = 0
    for t in range(len(TIPOS)):
        if errado_por_tipo[t] > maior_erro:
            maior_erro = errado_por_tipo[t]
            pior_tipo = t

    return [total, certo_kg, percentual, organico, adubo, na_rua, mais_comum, pior_tipo]


def recomendar(organico, adubo, na_rua, mais_comum, pior_tipo):
    """Recomendacao automatica que muda conforme os indicadores."""
    print("\n----- RECOMENDACAO -----")

    if mais_comum == 0 and adubo < organico:
        print("O organico e o lixo que a casa mais produz. Leve-o a um ponto de")
        print("compostagem: ele vira adubo para a horta comunitaria.")

    if na_rua > 0:
        print(f"ATENCAO: {na_rua:.1f} kg foram parar na rua ou em terreno.")
        print("Descarte na rua pode formar um ponto viciado. Consulte o ecoponto mais")
        print("proximo e confira quais materiais o local recebe.")

    if pior_tipo == -1:
        print("Todos os descartes foram certos. Parabens, continuem assim!")
    else:
        print(f"O tipo que a casa mais descarta errado e: {TIPOS[pior_tipo]}.")
        print("Dica: " + DICAS[pior_tipo])


def mostrar_relatorio():
    if len(tipos_reg) == 0:
        print("\nCadastre pelo menos um descarte para ver o relatorio.")
        return

    ind = calcular_indicadores()
    total = ind[0]
    certo_kg = ind[1]
    percentual = ind[2]
    organico = ind[3]
    adubo = ind[4]
    na_rua = ind[5]
    mais_comum = ind[6]
    pior_tipo = ind[7]

    print("\n===== RELATORIO DA CASA =====")
    print(f"Descartes registrados ............ {len(tipos_reg)}")
    print(f"Lixo total ....................... {total:.1f} kg")
    print(f"Media por descarte ............... {total / len(tipos_reg):.1f} kg")
    print(f"Descartado certo ................. {certo_kg:.1f} kg ({percentual:.0f}%)")
    print(f"Organico que poderia virar adubo . {organico:.1f} kg")
    print(f"Organico enviado a compostagem .. {adubo:.1f} kg")
    print(f"Jogado na rua/terreno ............ {na_rua:.1f} kg")
    print(f"Tipo de lixo mais comum .......... {TIPOS[mais_comum]}")
    print(f"Nivel da casa .................... {nivel(percentual)}")

    cheios = int(percentual // 10)
    print("Descarte certo: [" + "#" * cheios + "-" * (10 - cheios) + "]")

    recomendar(organico, adubo, na_rua, mais_comum, pior_tipo)


# ---------- programa principal ----------

def main():
    print("=" * 44)
    print("   CICLO VERDE - Diario de Descarte da Casa")
    print("=" * 44)
    print("Modelo didatico: confirme a aceitacao dos materiais no ponto de destino.")

    while True:
        print("\n1 - Cadastrar descarte")
        print("2 - Ver relatorio")
        print("3 - Ver lista de descartes")
        print("4 - Sair")
        opcao = ler_inteiro("Opcao: ", 1, 4)

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            mostrar_relatorio()
        elif opcao == 3:
            listar()
        else:
            print("Ate logo! Lixo no lugar certo vira horta.")
            break


if __name__ == "__main__":
    main()
