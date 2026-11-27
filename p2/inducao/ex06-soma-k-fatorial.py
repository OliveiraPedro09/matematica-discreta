# -*- coding: utf-8 -*-
# Exercicio 06 - Inducao com fatorial
# Fonte: lista de inducao (material/lista-inducao.png), Questao 05
#
# Provar que 1·1! + 2·2! + 3·3! + ... + n·n! = (n + 1)! - 1, para todo n >= 1
#
# O fatorial aqui e definido de forma RECURSIVA (igual a definicao da aula):
#   0! = 1             (base)
#   n! = n · (n - 1)!  (passo recursivo)
# Truque da prova: (k + 2)! = (k + 2) · (k + 1)!

import sys
sys.stdout.reconfigure(encoding="utf-8")


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def soma(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i * fatorial(i)
    return total


def formula(n):
    return fatorial(n + 1) - 1


print("=== Exercicio 06: 1·1! + 2·2! + ... + n·n! = (n + 1)! - 1 ===\n")

print("Conferencia numerica:")
print("   n | soma     | (n+1)! - 1")
for n in range(1, 9):
    print("  ", n, "|", str(soma(n)).rjust(8), "|", str(formula(n)).rjust(8),
          " ok" if soma(n) == formula(n) else " ERRO")
print()

passo_ok = True
for k in range(1, 201):
    if formula(k) + (k + 1) * fatorial(k + 1) != formula(k + 1):
        passo_ok = False
print("Passo indutivo formula(k) + (k+1)·(k+1)! = formula(k+1) para k = 1..200:", passo_ok)
print()

prova = """DEMONSTRACAO (PIM)

1) Base: n = 1
   lado esquerdo:  1·1! = 1
   lado direito:   (1 + 1)! - 1 = 2! - 1 = 2 - 1 = 1
   1 = 1  ∴ a base e verdadeira.

2) Hipotese de inducao (H.I.): vale para n = k, k >= 1
   1·1! + 2·2! + ... + k·k! = (k + 1)! - 1

3) Tese: vale para n = k + 1
   1·1! + 2·2! + ... + k·k! + (k + 1)·(k + 1)! = (k + 2)! - 1

   Demonstracao:
   1·1! + ... + k·k! + (k + 1)·(k + 1)!
   = (k + 1)! - 1 + (k + 1)·(k + 1)!          (H.I.)
   = (k + 1)! · [ 1 + (k + 1) ] - 1           (poe (k + 1)! em evidencia)
   = (k + 1)! · (k + 2) - 1
   = (k + 2)! - 1                             (definicao: (k + 2)! = (k + 2)·(k + 1)!)
   que e exatamente a tese.

∴ Pelo P.I.M., a formula vale para todo n >= 1."""
print(prova)
