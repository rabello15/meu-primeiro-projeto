caractere = input("Digite um caractere: ")
if caractere in "aeiouAEIOU":
    print(f"O caractere '{caractere}' é uma vogal.")
elif caractere.isalpha():
    print(f"O caractere '{caractere}' é uma consoante.")
elif caractere.isdigit():
    print(f"O caractere '{caractere}' é um número.")
else:
    print(f"O caractere '{caractere}' é um símbolo.")    
