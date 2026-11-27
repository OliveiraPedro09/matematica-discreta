# -*- coding: utf-8 -*-
# Exercicio 10 - Recursao: Torre de Hanoi
#
# Mover n discos da haste A para a C, usando B como auxiliar, sem nunca
# colocar um disco maior sobre um menor.
#
# Solucao recursiva:
#   n = 1: move o disco direto de A para C                     (base)
#   n > 1: move n-1 discos de A para B (usando C),
#          move o disco maior de A para C,
#          move os n-1 discos de B para C (usando A)            (passo recursivo)
#
# Numero de movimentos (definicao recursiva):
#   T(1) = 1
#   T(n) = 2·T(n - 1) + 1,  n >= 2
# Prove por inducao que T(n) = 2ⁿ - 1, para todo n >= 1.

import sys
sys.stdout.reconfigure(encoding="utf-8")

movimentos = []


def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        movimentos.append("disco 1: " + origem + " -> " + destino)
        return
    hanoi(n - 1, origem, auxiliar, destino)
    movimentos.append("disco " + str(n) + ": " + origem + " -> " + destino)
    hanoi(n - 1, auxiliar, destino, origem)


def T(n):
    if n == 1:
        return 1
    return 2 * T(n - 1) + 1


print("=== Exercicio 10: Torre de Hanoi, T(n) = 2ⁿ - 1 ===\n")

print("Movimentos para n = 3:")
hanoi(3, "A", "C", "B")
for i in range(len(movimentos)):
    print("   " + str(i + 1) + ".", movimentos[i])
print("   total:", len(movimentos), "movimentos")
print()

print("Contando movimentos x formula:")
print("    n | simulado | T(n) recursiva | 2ⁿ - 1")
for n in range(1, 11):
    movimentos = []
    hanoi(n, "A", "C", "B")
    print("   " + str(n).rjust(2), "|", str(len(movimentos)).rjust(8), "|",
          str(T(n)).rjust(14), "|", str(2 ** n - 1).rjust(6),
          " ok" if len(movimentos) == T(n) == 2 ** n - 1 else " ERRO")
print()

prova = """DEMONSTRACAO (PIM)

1) Base: n = 1
   T(1) = 1   e   2¹ - 1 = 1
   ∴ a base e verdadeira.

2) Hipotese de inducao (H.I.): vale para n = k, k >= 1
   T(k) = 2ᵏ - 1

3) Tese: vale para n = k + 1
   T(k + 1) = 2ᵏ⁺¹ - 1

   Demonstracao: pela definicao recursiva,
   T(k + 1) = 2·T(k) + 1
            = 2·(2ᵏ - 1) + 1          (H.I.)
            = 2ᵏ⁺¹ - 2 + 1
            = 2ᵏ⁺¹ - 1
   que e exatamente a tese.

∴ Pelo P.I.M., T(n) = 2ⁿ - 1 para todo n >= 1."""
print(prova)
