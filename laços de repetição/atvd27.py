palavra = input("Digite uma palavra: ").lower()
quantidade = 0

for letra in palavra:
    if letra in "aeiou":
        quantidade += 1

print("Quantidade de vogais:", quantidade)