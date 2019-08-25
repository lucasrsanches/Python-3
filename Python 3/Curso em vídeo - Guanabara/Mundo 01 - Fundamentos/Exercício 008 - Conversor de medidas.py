'''Escreva um valor em metros e o exiba
   convertido em centimetros e milímetros '''

valor = float(input("Digite um valor em metros: "))

print("Convertido para centimetros: ", valor*100, "cm")
print(f"Convertido para milímetros: {valor*1000:.2f} mm")
