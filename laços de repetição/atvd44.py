numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in reversed(numeros):
    print(numero)