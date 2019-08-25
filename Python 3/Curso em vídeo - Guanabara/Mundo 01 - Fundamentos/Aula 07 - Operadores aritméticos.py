n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

soma = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é {} \na subtração é {} \no produto é {}, a divisão é {:.2f}," .format(
    soma, sub, m, d), end=' ')
print("a divisão inteira é {} e a potência é {}". format(di, e))
