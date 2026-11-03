total = 0

while True:
    quantidade = int(input("Quantos doces deseja comprar? "))
    total += quantidade * 1.50

    continuar = input("Deseja continuar? ").lower()

    if continuar == "não" or continuar == "nao":
        break

print("Total final: R$", total)