n = int(input("Digite um número inteiro: "))

if n<= 1:
    print("O número não é primo.")
elif n in [2, 3, 5, 7]:
    print("O número é primo.")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("O número não é primo.")
else:
    print("O número é primo.")