quantidade = 0

while True:
    numero = int(input("Digite um número: "))

    if numero < 0:
        break

    quantidade += 1

print("Quantidade digitada:", quantidade)