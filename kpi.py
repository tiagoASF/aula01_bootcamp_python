#!/usr/bin/env python

""" Calcula o bônus anual total de um funcionário """
__version__ = "0.1.0"
__author__ = "Tiago Fialho"


BONUS_BASE = 1000.00

nome_funcionario = input("Informe o nome do funcionário: ")
salario = float(input(f"Salário do funcionário {nome_funcionario}: "))
percentual_bonus = float(input(f"Percentual do bônus: "))

kpi = BONUS_BASE + (salario * percentual_bonus)

print("Cálculo do bônus anual: Bônus fixo + salario * percentual.")
print(f"O bônus anula total do funcionário {nome_funcionario} é de R$ {round(kpi, 2)}")
