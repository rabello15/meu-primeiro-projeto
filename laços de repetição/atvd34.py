import random

secreto = random.randint(1, 50)
palpite = 0

while palpite != secreto:
    palpite = int(input("Adivinhe o número: "))

    if palpite < secreto:
        print("O número é maior!")
    elif palpite > secreto:
        print("O número é menor!")

print("Você acertou!")