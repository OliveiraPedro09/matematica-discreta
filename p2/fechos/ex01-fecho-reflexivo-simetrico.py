# -*- coding: utf-8 -*-
# Exercicio 01 - Fecho reflexivo e fecho simetrico
# Fonte: aula de 02/10 (Fechos de uma endorrelacao)
#
# A = { 1, 2, 3, 4 }   e   R = { <1,1>, <1,2>, <2,3> }  (endorrelacao em A)
#
# Fecho-Reflexivo(R) = R ∪ { <a,a> | a ∈ A }          -> poe os lacos que faltam
# Fecho-Simetrico(R) = R ∪ { <b,a> | <a,b> ∈ R }      -> poe as setas de volta
# Consequencia da definicao: R ⊆ Fecho-P(R) (o fecho nunca tira par nenhum)

import sys
sys.stdout.reconfigure(encoding="utf-8")

A = [1, 2, 3, 4]
R = [(1, 1), (1, 2), (2, 3)]


def texto(pares):
    return "{ " + ", ".join("<" + str(a) + "," + str(b) + ">" for a, b in sorted(pares)) + " }"


def mostrar_matriz(pares, A):
    print("         " + "  ".join(str(y) for y in A))
    for x in A:
        linha = []
        for y in A:
            if (x, y) in pares:
                linha.append("1")
            else:
                linha.append("0")
        print("      " + str(x) + " | " + "  ".join(linha))


def fecho_reflexivo(R, A):
    fecho = list(R)
    for a in A:
        if (a, a) not in fecho:
            fecho.append((a, a))
    return fecho


def fecho_simetrico(R):
    fecho = list(R)
    for a, b in R:
        if (b, a) not in fecho:
            fecho.append((b, a))
    return fecho


def contido(X, Y):
    for par in X:
        if par not in Y:
            return False
    return True


print("=== Exercicio 01: fecho reflexivo e fecho simetrico ===\n")
print("A =", A)
print("R =", texto(R))
print("Matriz de R:")
mostrar_matriz(R, A)
print()

# ---------------- fecho reflexivo ----------------
ref = fecho_reflexivo(R, A)
adicionados = [p for p in ref if p not in R]
print("a) Fecho reflexivo = R ∪ { <a,a> | a ∈ A }")
print("   diagonal de A      =", texto([(a, a) for a in A]))
print("   pares adicionados  =", texto(adicionados))
print("   Fecho-Reflexivo(R) =", texto(ref))
print("   (<1,1> ja estava em R, por isso nao foi adicionado de novo)")
print("   Matriz (diagonal toda com 1):")
mostrar_matriz(ref, A)
print("   R ⊆ Fecho-Reflexivo(R)?", contido(R, ref))
print()

# ---------------- fecho simetrico ----------------
sim = fecho_simetrico(R)
adicionados = [p for p in sim if p not in R]
print("b) Fecho simetrico = R ∪ R⁻¹  (R⁻¹ = inverte cada par)")
print("   R⁻¹                =", texto([(b, a) for a, b in R]))
print("   pares adicionados  =", texto(adicionados))
print("   Fecho-Simetrico(R) =", texto(sim))
print("   (<1,1> e o proprio inverso, nao gera par novo)")
print("   Matriz (espelhada na diagonal: M = Mᵀ):")
mostrar_matriz(sim, A)
print("   R ⊆ Fecho-Simetrico(R)?", contido(R, sim))
print()
print("Grafo: reflexivo = todo vertice ganha laco; simetrico = toda seta ganha volta.")
print("O vertice 4 nao aparece em R, entao no simetrico ele continua isolado.")
