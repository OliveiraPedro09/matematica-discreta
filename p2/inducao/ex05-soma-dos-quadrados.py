# -*- coding: utf-8 -*-
# Exercicio 05 - Inducao: soma dos quadrados
# Fonte: lista de inducao (material/lista-inducao.png), Questao 01
#
# Provar que 1² + 2² + 3² + ... + n² = (n/6)(n + 1)(2n + 1), para todo n >= 1
#
# O programa (1) confere a formula para varios n, (2) confere o passo
# "formula(k) + (k+1)² = formula(k+1)" e (3) imprime a demonstracao.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def soma(n):                      # lado esquerdo: soma termo a termo
    total = 0
    for i in range(1, n + 1):
        total = total + i * i
    return total


def formula(n):                   # lado direito (o produto sempre e multiplo de 6)
    return n * (n + 1) * (2 * n + 1) // 6


print("=== Exercicio 05: 1² + 2² + ... + n² = n(n+1)(2n+1)/6 ===\n")

print("Conferencia numerica:")
print("   n | soma | formula")
for n in range(1, 9):
    print("  ", n, "|", str(soma(n)).rjust(4), "|", str(formula(n)).rjust(5),
          " ok" if soma(n) == formula(n) else " ERRO")
print()

passo_ok = True
for k in range(1, 501):
    if formula(k) + (k + 1) ** 2 != formula(k + 1):
        passo_ok = False
print("Passo indutivo formula(k) + (k+1)² = formula(k+1) para k = 1..500:", passo_ok)
print()

prova = """DEMONSTRACAO (PIM)

1) Base: n = 1
   lado esquerdo:  1² = 1
   lado direito:   (1/6)(1 + 1)(2·1 + 1) = (1/6)·2·3 = 1
   1 = 1  ∴ a base e verdadeira.

2) Hipotese de inducao (H.I.): vale para n = k, k >= 1
   1² + 2² + ... + k² = k(k + 1)(2k + 1)/6

3) Tese: vale para n = k + 1
   1² + 2² + ... + k² + (k + 1)² = (k + 1)(k + 2)(2k + 3)/6

   Demonstracao:
   1² + ... + k² + (k + 1)²
   = k(k + 1)(2k + 1)/6 + (k + 1)²                  (H.I.)
   = (k + 1) · [ k(2k + 1) + 6(k + 1) ] / 6         (poe (k + 1) em evidencia)
   = (k + 1) · [ 2k² + k + 6k + 6 ] / 6
   = (k + 1) · (2k² + 7k + 6) / 6
   = (k + 1)(k + 2)(2k + 3)/6                       (2k² + 7k + 6 = (k + 2)(2k + 3))
   que e exatamente a tese.

∴ Pelo P.I.M., a formula vale para todo n >= 1."""
print(prova)
print()
print("Dica: para fatorar 2k² + 7k + 6, procure as raizes (k = -2 e k = -3/2)")
print("ou teste: (k + 2)(2k + 3) = 2k² + 3k + 4k + 6 = 2k² + 7k + 6.")
