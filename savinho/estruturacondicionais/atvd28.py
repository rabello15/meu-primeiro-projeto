caractere = input("Digite um caractere: ")
codigo = ord(caractere)
if 65 <= codigo <= 90:
    print("O caractere é uma letra maiúscula.")
elif 97 <= codigo <= 122:
    print("O caractere é uma letra minúscula.")
elif 48 <= codigo <= 57:
    print("O caractere é um número.")
else:
    print("É outro simbolo.")