# -*- coding: utf-8 -*-
# Exercicio 09 - Sequencia definida por recursao + prova por inducao
# Fonte: aula de 12/11, Partes 1 a 3
#
# Seja a sequencia a₁, a₂, ... definida como
#   a₁ = 3                          (base)
#   aₖ = 7·aₖ₋₁,  k ∈ N e k >= 2    (passo recursivo)
# Prove por inducao matematica que aₙ = 3·7ⁿ⁻¹, para todo n ∈ N*.
#
# A definicao recursiva diz COMO calcular um termo a partir do anterior.
# A formula fechada (3·7ⁿ⁻¹) calcula direto. A inducao prova que as duas
# dao sempre o mesmo valor.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def a_recursiva(n):
    if n == 1:
        return 3                       # base
    return 7 * a_recursiva(n - 1)      # passo recursivo


def a_fechada(n):
    return 3 * 7 ** (n - 1)


def a_com_rastro(n, nivel=0):
    # mostra as chamadas recursivas "descendo" ate a base e "voltando"
    recuo = "   " * nivel
    if n == 1:
        print(recuo + "a(1) = 3   <- base, para aqui")
        return 3
    print(recuo + "a(" + str(n) + ") = 7 · a(" + str(n - 1) + ")")
    valor = 7 * a_com_rastro(n - 1, nivel + 1)
    print(recuo + "a(" + str(n) + ") = " + str(valor))
    return valor


print("=== Exercicio 09: a₁ = 3, aₖ = 7·aₖ₋₁  =>  aₙ = 3·7ⁿ⁻¹ ===\n")

print("Como o computador calcula a(4) pela recursao:")
a_com_rastro(4)
print()

print("Comparando recursiva x formula fechada:")
print("   n | recursiva  | 3·7ⁿ⁻¹")
for n in range(1, 9):
    print("  ", n, "|", str(a_recursiva(n)).rjust(10), "|", str(a_fechada(n)).rjust(10),
          " ok" if a_recursiva(n) == a_fechada(n) else " ERRO")
print()

prova = """DEMONSTRACAO (PIM)

1) Base: n = 1
   a₁ = 3·7¹⁻¹ = 3·7⁰ = 3·1 = 3
   e pela definicao a₁ = 3  ∴ o passo base e verdadeiro.

2) Hipotese de inducao (H.I.): vale para n = k, k ∈ N*
   aₖ = 3·7ᵏ⁻¹   (e aceita como verdadeira)

3) Tese: vale para n = k + 1
   aₖ₊₁ = 3·7⁽ᵏ⁺¹⁾⁻¹ = 3·7ᵏ

   Demonstracao: sabe-se, da definicao da sequencia, que
   aₖ₊₁ = 7·a₍ₖ₊₁₎₋₁ = 7·aₖ
        = 7·(3·7ᵏ⁻¹)                   (H.I.)
        = 3·7¹⁺ᵏ⁻¹
        = 3·7ᵏ
   que e exatamente a tese.

∴ Pelo P.I.M., P(n) e verdadeira para todo n ∈ N*."""
print(prova)
print()
print("Padrao para esse tipo de questao: na tese, use a DEFINICAO RECURSIVA")
print("para escrever aₖ₊₁ em funcao de aₖ, e ai troque aₖ pela H.I.")
