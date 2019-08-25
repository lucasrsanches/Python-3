'''Faça um programa que leia um número inteiro
   e mostre na tela o seu sucessor e seu antecessor
'''
n1 = int(input("Digite um número inteiro: "))

print("O antecessor do número %d é " % (n1), end='')
print(f"{n1-1} e o seu sucessor é {n1+1}")
