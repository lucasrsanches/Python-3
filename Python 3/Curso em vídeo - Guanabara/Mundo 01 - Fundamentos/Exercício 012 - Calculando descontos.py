'''Faça um algoritmo que leia o preço de um produto
   e mostre seu novo preço, com 5% de desconto '''

compra = float(input("Valor do produto R$: "))

print(
    f"A compra R${compra}, com o desconto de 5% irá ficar por R${compra-compra*(5/100)}")
