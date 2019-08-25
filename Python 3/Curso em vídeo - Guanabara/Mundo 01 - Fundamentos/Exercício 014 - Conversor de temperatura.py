'''Escreva um programa que converta uma temperatura
   digitada em ºC e converta para ºF.
   Formula = (°C × 9/5) + 32 = ºF '''

temp = float(input("Temperatura atual em ºC: "))

print(f"A temperatura {temp}ºC convertida ficará em {(temp * 9/5) + 32}ºF")
