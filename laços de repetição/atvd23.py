valor = int(input("Digite o valor do saque: "))

for nota in [100, 50, 20, 10, 5]:
    quantidade = valor // nota
    print("Notas de", nota, ":", quantidade)
    valor %= nota