secreto = 7

for i in range(3):
    numero = int(input("Adivinhe o número: "))

    if numero == secreto:
        print("Você acertou!")
        break
else:
    print("Você perdeu! Acabaram as tentativas.")