nomes = []

while True:
    nome = input("Digite um nome ou sair: ")

    if nome.lower() == "sair":
        break

    nomes.append(nome)

print("Nomes digitados:")

for nome in nomes:
    print(nome)