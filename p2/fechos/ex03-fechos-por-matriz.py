# -*- coding: utf-8 -*-
# Exercicio 03 - Propriedades e os tres fechos pela matriz
# Fonte: Apostila de Fechos, lista de fixacao, exercicio 3
#
# A = { 1, 2, 3 } e M = | 0 1 0 |
#                       | 1 0 1 |
#                       | 0 0 0 |
#
# Fecho reflexivo:  M ∨ I          (OU com a identidade)
# Fecho simetrico:  M ∨ Mᵀ         (OU com a transposta)
# Fecho transitivo: M ∨ M² ∨ M³    (potencias booleanas ate n = 3)
# Produto booleano: troca "vezes" por E (∧) e "mais" por OU (∨)

import sys
sys.stdout.reconfigure(encoding="utf-8")

M = [[0, 1, 0],
     [1, 0, 1],
     [0, 0, 0]]
n = len(M)


def mostrar(nome, X):
    print("   " + nome)
    print("         1  2  3")
    for i in range(n):
        print("      " + str(i + 1) + " | " + "  ".join(str(v) for v in X[i]))


def identidade():
    I = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(1 if i == j else 0)
        I.append(linha)
    return I


def ou(X, Y):
    Z = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(1 if (X[i][j] == 1 or Y[i][j] == 1) else 0)
        Z.append(linha)
    return Z


def transposta(X):
    T = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(X[j][i])
        T.append(linha)
    return T


def produto_booleano(X, Y):
    # (X ⊙ Y)[i][j] = 1 se existe k com X[i][k] = 1 E Y[k][j] = 1
    Z = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = 0
            for k in range(n):
                if X[i][k] == 1 and Y[k][j] == 1:
                    valor = 1
            linha.append(valor)
        Z.append(linha)
    return Z


print("=== Exercicio 03: fechos pela matriz ===\n")
mostrar("M =", M)
print()

# ---------------- propriedades ----------------
reflexiva = all(M[i][i] == 1 for i in range(n))
simetrica = (M == transposta(M))
M2 = produto_booleano(M, M)
transitiva = (ou(M, M2) == M)          # transitiva <=> M² nao cria 1 novo

print("Propriedades:")
print("   reflexiva?", reflexiva, " -> diagonal tem 0 (falta <1,1>, <2,2>, <3,3>)")
print("   simetrica?", simetrica, " -> M[2][3] = 1 mas M[3][2] = 0 (<2,3> sem <3,2>)")
print("   transitiva?", transitiva, " -> <1,2> e <2,1> exigiriam <1,1>")
print()

# ---------------- fechos ----------------
mostrar("a) Fecho reflexivo  M ∨ I =", ou(M, identidade()))
print()
mostrar("Mᵀ (transposta) =", transposta(M))
mostrar("b) Fecho simetrico  M ∨ Mᵀ =", ou(M, transposta(M)))
print()

M3 = produto_booleano(M2, M)
mostrar("M² = M ⊙ M  (caminhos de 2 passos) =", M2)
mostrar("M³ = M² ⊙ M (caminhos de 3 passos) =", M3)
mostrar("c) Fecho transitivo  M ∨ M² ∨ M³ =", ou(ou(M, M2), M3))
print()
print("Leitura do M²: 1->2->1 da <1,1>, 1->2->3 da <1,3>, 2->1->2 da <2,2>.")
print("A linha 3 fica zerada: o 3 nao tem seta saindo, nao alcanca ninguem.")
print()
print("ATENCAO: o gabarito da apostila poe a linha 3 do fecho transitivo como 0 0 1.")
print("Isso esta errado: <3,3> so entraria se existisse caminho 3 -> ... -> 3,")
print("e o 3 nao tem nenhuma seta saindo. O certo e 0 0 0 (confira M² e M³ acima).")
