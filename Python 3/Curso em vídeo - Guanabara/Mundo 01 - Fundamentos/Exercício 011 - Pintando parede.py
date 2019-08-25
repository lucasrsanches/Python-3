'''Faça um programa que leia a largura e a altura
   de uma parede em metros, calcule a sua área e a
   quantidade de tinta necessária para pintá-lo, sabendo
   que cada litro de tinta pinta uma área de 2m² '''

largura = float(input("Largura da parede em metros: "))
altura = float(input("Altura da parede em metros: "))

area = largura*altura
tinta = area/2

print(f"A área é: {area:.2f}m²")
print("Para pintar esta parede será necessário {}L de tinta".format(tinta))
