# -*- coding: utf-8 -*-
# Exercicio 04 - Fecho transitivo pelo algoritmo de Warshall
# Fonte: Apostila de Fechos, lista de fixacao, exercicio 5
#
# A = { 1, 2, 3, 4 } e R = { <1,2>, <2,3>, <3,4>, <4,1> }  (ciclo 1->2->3->4->1)
# Pergunta: R e reflexiva? simetrica? Qual o fecho transitivo? Ele e reflexivo? Quantos pares?
#
# Warshall: para k = 1..n, para i = 1..n, para j = 1..n:
#     W[i][j] = W[i][j] OU (W[i][k] E W[k][j])
# Ideia: na etapa k, o vertice k passa a poder ser usado como "ponte" (intermediario).

import sys
sys.stdout.reconfigure(encoding="utf-8")

A = [1, 2, 3, 4]
R = [(1, 2), (2, 3), (3, 4), (4, 1)]
n = len(A)


def mostrar(W, novos):
    print("         1   2   3   4")
    for i in range(n):
        linha = []
        for j in range(n):
            if (i, j) in novos:
                linha.append(str(W[i][j]) + "*")     # * = virou 1 nesta etapa
            else:
                linha.append(str(W[i][j]) + " ")
        print("      " + str(i + 1) + " | " + "  ".join(linha))


print("=== Exercicio 04: algoritmo de Warshall ===\n")

reflexiva = all((a, a) in R for a in A)
simetrica = all((b, a) in R for a, b in R)
print("R =", R)
print("reflexiva?", reflexiva, " (nao tem nenhum laco)")
print("simetrica?", simetrica, " (tem <1,2> mas nao <2,1>)")
print()

# monta a matriz inicial W0 = M_R
W = []
for x in A:
    linha = []
    for y in A:
        linha.append(1 if (x, y) in R else 0)
    W.append(linha)

print("W0 = matriz de R")
mostrar(W, [])
print()

for k in range(n):
    novos = []
    for i in range(n):
        for j in range(n):
            if W[i][j] == 0 and W[i][k] == 1 and W[k][j] == 1:
                novos.append((i, j))
    for i, j in novos:
        W[i][j] = 1
    print("W" + str(k + 1) + " = usando o vertice", k + 1, "como ponte  (* = novo)")
    for i, j in novos:
        print("      ", i + 1, "->", k + 1, "->", j + 1, " gera <" + str(i + 1) + "," + str(j + 1) + ">")
    mostrar(W, novos)
    print()

pares = []
for i in range(n):
    for j in range(n):
        if W[i][j] == 1:
            pares.append((i + 1, j + 1))

print("Fecho transitivo =", pares)
print("Quantidade de pares:", len(pares), "(= 4² = 16, ou seja, A × A inteiro)")
print("O fecho e reflexivo?", all(W[i][i] == 1 for i in range(n)))
print()
print("Por que? No ciclo todo vertice alcanca todos os outros e volta para si")
print("mesmo dando a volta (ex.: 1->2->3->4->1 gera <1,1>).")
