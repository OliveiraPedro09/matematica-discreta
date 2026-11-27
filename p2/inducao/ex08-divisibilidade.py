# -*- coding: utf-8 -*-
# Exercicio 08 - Inducao com divisibilidade
# Fonte: aula de 12/11, Parte 4
#
# Mostre, por inducao, que n³ + 2n e divisivel por 3, para todo n ∈ N (n >= 0)
#
# "Divisivel por 3" se escreve como: existe m inteiro com n³ + 2n = 3m.
# Truque da prova: expandir (k + 1)³ = k³ + 3k² + 3k + 1 e achar o k³ + 2k da H.I.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def P(n):
    return n ** 3 + 2 * n


print("=== Exercicio 08: n³ + 2n e divisivel por 3 ===\n")

print("Conferencia numerica (m = (n³ + 2n) / 3):")
print("   n | n³ + 2n | m")
for n in range(0, 9):
    print("  ", n, "|", str(P(n)).rjust(7), "|", P(n) // 3,
          "" if P(n) % 3 == 0 else "  NAO DIVIDE")
print()

print("Diferenca entre um termo e o anterior: P(k+1) - P(k) = 3(k² + k + 1)")
diferenca_ok = True
for k in range(0, 501):
    if P(k + 1) - P(k) != 3 * (k * k + k + 1):
        diferenca_ok = False
print("   conferido para k = 0..500:", diferenca_ok)
print("   (e isso que a prova mostra: somar um multiplo de 3 a um multiplo de 3)")
print()

prova = """DEMONSTRACAO (PIM)

1) Base: n = 0
   P(0): 0³ + 2·0 = 0   e   0 = 3·0
   ∴ a base e satisfeita (0 e divisivel por 3).

2) Hipotese de inducao (H.I.): vale para n = k, k ∈ N
   k³ + 2k = 3m, para algum m inteiro

3) Tese: vale para n = k + 1
   (k + 1)³ + 2(k + 1) e divisivel por 3

   Demonstracao:
   (k + 1)³ + 2(k + 1)
   = k³ + 3k² + 3k + 1 + 2k + 2           ((k + 1)³ = k³ + 3k² + 3k + 1)
   = (k³ + 2k) + 3k² + 3k + 3             (agrupa o que tem na H.I.)
   = 3m + 3k² + 3k + 3                    (H.I.)
   = 3(m + k² + k + 1)
   Como m + k² + k + 1 e inteiro, o resultado e divisivel por 3.

∴ Pelo P.I.M., n³ + 2n e divisivel por 3 para todo n ∈ N."""
print(prova)
