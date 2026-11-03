maior = float("-inf")
menor = float("inf")

for i in range(10):
    numero = float(input("Digite um número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Maior:", maior)
print("Menor:", menor)