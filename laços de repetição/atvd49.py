import random

maior = 0

for i in range(10):
    numero = random.randint(1, 100)
    print(numero)

    if numero > maior:
        maior = numero

print("Maior número:", maior)