# -*- coding: utf-8 -*-
# Exercicio 07 - Inducao com desigualdade
# Fonte: lista de inducao (material/lista-inducao.png), Questao 10
#
# Provar que n! > 3ⁿ, para todo n >= 7
#
# Em desigualdade, a base NAO e 1: e o primeiro n em que a afirmacao vale.
# O programa mostra a tabela, a demonstracao e depois testa a base das
# outras desigualdades da lista (Q08, Q15, Q16, Q17), porque duas delas
# estao com a base errada no enunciado.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


print("=== Exercicio 07: n! > 3ⁿ para n >= 7 ===\n")

print("Por que comecar em 7?")
print("   n |   n!   |  3ⁿ   | n! > 3ⁿ ?")
for n in range(1, 10):
    print("  ", n, "|", str(fatorial(n)).rjust(6), "|", str(3 ** n).rjust(5), "|",
          "V" if fatorial(n) > 3 ** n else "F")
print("   -> so passa a valer em n = 7 (5040 > 2187).")
print()

passo_ok = True
for k in range(7, 301):
    # o passo usa: (k+1)! = (k+1)·k! > (k+1)·3^k >= 3·3^k = 3^(k+1)
    if not ((k + 1) * 3 ** k >= 3 ** (k + 1) and fatorial(k + 1) > 3 ** (k + 1)):
        passo_ok = False
print("Conferencia do passo para k = 7..300:", passo_ok)
print()

prova = """DEMONSTRACAO (PIM)

1) Base: n = 7
   7! = 5040   e   3⁷ = 2187
   5040 > 2187  ∴ a base e verdadeira.

2) Hipotese de inducao (H.I.): vale para n = k, k >= 7
   k! > 3ᵏ

3) Tese: vale para n = k + 1
   (k + 1)! > 3ᵏ⁺¹

   Demonstracao:
   (k + 1)! = (k + 1) · k!
            > (k + 1) · 3ᵏ        (H.I., multiplicando os dois lados por k + 1 > 0)
            > 3 · 3ᵏ              (pois k >= 7  =>  k + 1 >= 8 > 3)
            = 3ᵏ⁺¹
   Logo (k + 1)! > 3ᵏ⁺¹, que e a tese.

∴ Pelo P.I.M., n! > 3ⁿ para todo n >= 7."""
print(prova)
print()

# ------------------------------------------------------------------
print("=== Bonus: conferindo a base das outras desigualdades da lista ===\n")
testes = [
    ("Q08: 2ⁿ > n²      (lista diz n > 3, ou seja, n >= 4)", 4, lambda n: 2 ** n > n * n),
    ("Q15: n² > 2n + 3  (lista diz n >= 3)", 3, lambda n: n * n > 2 * n + 3),
    ("Q16: n² > n + 1   (lista diz n >= 2)", 2, lambda n: n * n > n + 1),
    ("Q17: n! > n²      (lista diz n >= 4)", 4, lambda n: fatorial(n) > n * n),
]
for titulo, base, teste in testes:
    print(titulo)
    if teste(base):
        print("   base n =", base, "OK")
    else:
        n = base
        while not teste(n):
            n = n + 1
        print("   base n =", base, "FALHA! A afirmacao so vale a partir de n =", n)
print()
print("Q08: em n = 4 da 2⁴ = 16 e 4² = 16 -> 16 > 16 e FALSO. Base certa: n = 5.")
print("Q15: em n = 3 da 3² = 9 e 2·3 + 3 = 9 -> 9 > 9 e FALSO. Base certa: n = 4.")
print("Se cair assim na prova, mostre que a base falha e prove a partir do n correto.")
