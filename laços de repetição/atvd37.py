total = 0

while True:
    preco = float(input("Digite o preço do produto (0 para parar): "))

    if preco == 0:
        break

    total += preco

print("Total da compra: R$", total)