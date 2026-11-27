# -*- coding: utf-8 -*-
# Exercicio 02 - Fecho transitivo pela definicao indutiva
# Fonte: aula de 02/10 (Fechos de uma endorrelacao)
#
# Definicao indutiva do Fecho-Transitivo(R):
#   1) se <a,b> ∈ R, entao <a,b> ∈ Fecho-Transitivo(R)
#   2) se <a,b> e <b,c> ∈ Fecho-Transitivo(R), entao <a,c> ∈ Fecho-Transitivo(R)
#   Obs.: os unicos elementos do fecho sao os construidos pelas regras acima.
#
# a) A = { 1, 2, 3, 4, 5 },  R = { <1,2>, <1,5>, <2,3>, <3,4> }
# b) A = { 1, 2, 3, 4 },     R = { <1,2>, <1,3>, <2,3>, <3,4>, <4,2> }  (tem ciclo 2->3->4->2)
#
# O programa aplica a regra 2 em "rodadas": um par novo pode criar outro
# encadeamento, entao so para quando uma rodada inteira nao acrescentar nada.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def par(p):
    return "<" + str(p[0]) + "," + str(p[1]) + ">"


def texto(pares):
    return "{ " + ", ".join(par(p) for p in sorted(pares)) + " }"


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


def fecho_transitivo(R):
    fecho = list(R)                       # regra 1
    rodada = 1
    while True:
        novos = []
        motivos = []
        for a, b in fecho:                # regra 2
            for c, d in fecho:
                if b == c and (a, d) not in fecho and (a, d) not in novos:
                    novos.append((a, d))
                    motivos.append(par((a, b)) + " e " + par((c, d)) + " => " + par((a, d)))
        if len(novos) == 0:
            print("   rodada", rodada, ": nenhum par novo -> fim")
            break
        print("   rodada", rodada, ":")
        for m in motivos:
            print("      ", m)
        fecho = fecho + novos
        rodada = rodada + 1
    return fecho


def transitiva(R):
    for a, b in R:
        for c, d in R:
            if b == c and (a, d) not in R:
                return False
    return True


def resolver(titulo, A, R):
    print(titulo)
    print("   A =", A)
    print("   R =", texto(R), "  transitiva?", transitiva(R))
    fecho = fecho_transitivo(R)
    print("   Fecho-Transitivo(R) =", texto(fecho))
    print("   total de pares:", len(fecho), "  transitiva agora?", transitiva(fecho))
    print("   Matriz:")
    mostrar_matriz(fecho, A)
    print()


print("=== Exercicio 02: fecho transitivo ===\n")

resolver("a) sem ciclo", [1, 2, 3, 4, 5], [(1, 2), (1, 5), (2, 3), (3, 4)])

resolver("b) com ciclo 2 -> 3 -> 4 -> 2", [1, 2, 3, 4],
         [(1, 2), (1, 3), (2, 3), (3, 4), (4, 2)])

print("Repare no item b: como 2, 3 e 4 estao num ciclo, cada um alcanca o outro")
print("e tambem volta para si mesmo. Por isso aparecem <2,2>, <3,3> e <4,4>")
print("mesmo sem pedir fecho reflexivo. O 1 nao recebe <1,1> porque ninguem volta ao 1.")
