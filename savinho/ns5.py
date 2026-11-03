prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))
media = (prova1 + prova2 + prova3) / 3
if media >= 6:
    print(f"Parabéns! Você foi aprovado com média .")
elif media >= 5:
    print(f"voce esta em recuperação,vai dar certo.")
else:
    print(f"Você está de recuperação com média.")  