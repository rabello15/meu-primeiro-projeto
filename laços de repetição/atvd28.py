frase = input("Digite uma frase: ")
quantidade = 0

for caractere in frase:
    if caractere == " ":
        quantidade += 1

print("Quantidade de espaços:", quantidade)