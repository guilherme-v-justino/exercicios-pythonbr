"""Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês. """

valor_hora = float(input("Quanto você ganha por hora? :"))
horas_trabalhadas = int(input("Quantas horas você trabalhou este mês? :"))

print(f'O seu salário este mês foi: {valor_hora * horas_trabalhadas} reais')
