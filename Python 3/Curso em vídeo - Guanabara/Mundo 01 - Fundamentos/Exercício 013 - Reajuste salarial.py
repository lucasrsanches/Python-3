'''Faça um algoritmo que leia o salário de um funcionário
   e mostre seu novo salário, com 15% de aumento '''

salario = float(input("Digite seu salário atual R$:"))

print(
    f"Seu salário com 15% de aumento será de R${salario*(15/100)+salario:.2f}")
