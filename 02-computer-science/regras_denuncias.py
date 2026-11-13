# Regras de decisao do Painel do Bairro - Ciclo Verde
# Global Solution 2026.2 - Computer Science - Turma 1CCPR
# Gustavo Fidelis de Souza e Silva (RM 574666) | Rafael Meirelles (RM 574897) | Anna Luisa Lima (RM 575081)
#
# Cada denuncia de lixo na rua e descrita por variaveis que valem 0 ou 1:
#   E = tem entulho na calcada               (1 = sim, 0 = nao)
#   P = perto de escola ou posto de saude    (1 = sim, 0 = nao)
#   B = bloqueia a passagem de pedestres     (1 = sim, 0 = nao)
#   L = o lugar ja foi limpo antes           (1 = sim, 0 = nao)
#   V = o lixo voltou em ate 7 dias          (1 = sim, 0 = nao)
#   F = a denuncia tem foto                  (1 = sim, 0 = nao)
#   D = a denuncia tem endereco              (1 = sim, 0 = nao)
#
# Regras:
#   R1 Urgente                = E AND (P OR B)
#   R2 Ponto viciado          = L AND V
#   R3 Cadastro inconsistente = F XOR D
#   R4 Pode arquivar          = (NOT E) AND (NOT V)
#
# Como rodar:  python regras_denuncias.py


# ---------- as regras (uma funcao por regra) ----------

def urgente(e, p, b):
    return e and (p or b)


def ponto_viciado(l, v):
    return l and v


def cadastro_inconsistente(f, d):
    return f ^ d          # ^ e o XOR: 1 so quando as duas entradas sao diferentes


def pode_arquivar(e, v):
    return (not e) and (not v)


# ---------- entrada ----------

def ler_bit(pergunta):
    """Pede 0 ou 1 ate o usuario digitar certo."""
    while True:
        resposta = input(pergunta + " (0 ou 1): ").strip()
        if resposta == "0" or resposta == "1":
            return int(resposta)
        print("  Digite apenas 0 ou 1.")


def avaliar_uma_denuncia():
    print("\nResponda sobre a denuncia:")
    e = ler_bit("E - Tem entulho na calcada?")
    p = ler_bit("P - Fica perto de escola ou posto de saude?")
    b = ler_bit("B - Bloqueia a passagem de pedestres?")
    l = ler_bit("L - O lugar ja foi limpo antes?")
    v = ler_bit("V - O lixo voltou em ate 7 dias?")
    f = ler_bit("F - A denuncia tem foto?")
    d = ler_bit("D - A denuncia tem endereco?")

    r1 = int(urgente(e, p, b))
    r2 = int(ponto_viciado(l, v))
    r3 = int(cadastro_inconsistente(f, d))
    r4 = int(pode_arquivar(e, v))

    print("\n===== RESULTADO =====")
    print(f"R1 Urgente ................ {r1}")
    print(f"R2 Ponto viciado .......... {r2}")
    print(f"R3 Cadastro inconsistente . {r3}")
    print(f"R4 Pode arquivar .......... {r4}")

    print("\nO que o painel faz:")
    if f == 0 and d == 0:
        print("- Denuncia sem foto e sem endereco: descartada.")
        return
    if r3 == 1:
        print("- Pedir ao morador a informacao que falta (foto ou endereco).")
    if r1 == 1:
        print("- Mandar equipe de limpeza HOJE.")
    if r2 == 1:
        print("- Marcar no mapa como ponto viciado e acompanhar.")
    if r4 == 1:
        print("- Pode arquivar a denuncia.")
    if r1 == 0 and r2 == 0 and r3 == 0 and r4 == 0:
        print("- Entrar na fila normal de limpeza.")


# ---------- teste de todas as combinacoes ----------
# Para conferir com as tabelas-verdade feitas a mao e com os circuitos do simulador.

def testar_todas():
    print("\nR1 Urgente = E AND (P OR B)")
    print(" E P B | R1")
    for e in (0, 1):
        for p in (0, 1):
            for b in (0, 1):
                print(f" {e} {p} {b} |  {int(urgente(e, p, b))}")

    print("\nR2 Ponto viciado = L AND V")
    print(" L V | R2")
    for l in (0, 1):
        for v in (0, 1):
            print(f" {l} {v} |  {int(ponto_viciado(l, v))}")

    print("\nR3 Cadastro inconsistente = F XOR D")
    print(" F D | R3")
    for f in (0, 1):
        for d in (0, 1):
            print(f" {f} {d} |  {int(cadastro_inconsistente(f, d))}")

    print("\nR4 Pode arquivar = (NOT E) AND (NOT V)")
    print(" E V | R4")
    for e in (0, 1):
        for v in (0, 1):
            print(f" {e} {v} |  {int(pode_arquivar(e, v))}")


# ---------- programa principal ----------

def main():
    print("=" * 46)
    print("  CICLO VERDE - Regras do Painel do Bairro")
    print("=" * 46)
    while True:
        print("\n1 - Avaliar uma denuncia")
        print("2 - Testar todas as combinacoes")
        print("3 - Sair")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            avaliar_uma_denuncia()
        elif opcao == "2":
            testar_todas()
        elif opcao == "3":
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
