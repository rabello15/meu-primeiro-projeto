media = float(input("Digite a média do aluno: "))
faltas = int(input("Digite a quantidade de faltas: "))

if media >= 7 and faltas <= 10:
    print("Aluno Aprovado.")
elif media >= 5 and faltas <= 10:
    print("Aluno em Recuperação.")
else:
    print("Aluno Reprovado.")