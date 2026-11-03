nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
mediaponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

if mediaponderada >= 7:
    print("Aluno aprovado.")
elif mediaponderada >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")