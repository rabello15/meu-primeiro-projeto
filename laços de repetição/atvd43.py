inicio = int(input("Digite o primeiro valor: "))
fim = int(input("Digite o segundo valor: "))
soma = 0

for i in range(inicio, fim + 1):
    if i % 2 != 0:
        soma += i

print("Soma dos ímpares:", soma)