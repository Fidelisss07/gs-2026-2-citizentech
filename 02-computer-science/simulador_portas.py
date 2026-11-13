"""Simulador local de circuitos combinacionais definidos em circuitos.json.
Cada porta e avaliada por sua tabela de verdade; nao usa as expressoes do programa do grupo.
Executar: python simulador_portas.py
"""
from pathlib import Path
from itertools import product
import json
import regras_denuncias as grupo

PORTAS = {
    "AND": {(0,0):0,(0,1):0,(1,0):0,(1,1):1},
    "OR": {(0,0):0,(0,1):1,(1,0):1,(1,1):1},
    "XOR": {(0,0):0,(0,1):1,(1,0):1,(1,1):0},
    "NOT": {(0,):1,(1,):0},
}

def simular(circuito, entradas):
    if set(entradas) != set(circuito["inputs"]):
        raise ValueError("Entradas diferentes das definidas no circuito")
    if any(v not in (0,1) for v in entradas.values()):
        raise ValueError("Entradas devem ser bits")
    sinais = dict(entradas)
    for saida, porta, fios in circuito["gates"]:
        bits = tuple(sinais[nome] for nome in fios)
        sinais[saida] = PORTAS[porta][bits]
    return sinais[circuito["output"]], sinais

def validar():
    nets=json.loads(Path(__file__).with_name("circuitos.json").read_text(encoding="utf-8"))
    funcoes={"R1":grupo.urgente,"R2":grupo.ponto_viciado,
             "R3":grupo.cadastro_inconsistente,"R4":grupo.pode_arquivar}
    resultados=[]
    for regra,net in nets.items():
        for bits in product((0,1),repeat=len(net["inputs"])):
            entradas=dict(zip(net["inputs"],bits))
            saida,sinais=simular(net,entradas)
            python=int(funcoes[regra](*bits))
            assert saida==python, (regra,entradas,saida,python)
            resultados.append({"regra":regra,"entradas":entradas,"sinais":sinais,
                               "circuito":saida,"python":python,"confere":True})
    return resultados

if __name__ == "__main__":
    for r in validar():
        entradas=" ".join(f"{k}={v}" for k,v in r["entradas"].items())
        sinais=" ".join(f"{k}={v}" for k,v in r["sinais"].items() if k not in r["entradas"])
        print(f"{r['regra']} | {entradas} | {sinais} | Python={r['python']} | OK")
    print("20/20 combinacoes conferem: portas conectadas x implementacao Python")
