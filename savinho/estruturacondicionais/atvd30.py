n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))

maior = max(n1, n2, n3, n4)
menor = min(n1, n2, n3, n4)
soma = n1 + n2 + n3 + n4

media = (soma - maior - menor) / 2
print(f"Média calculada: {media:.2f}")

if media >= 7:
    print("Classificação: Aprovado")
elif media >= 5:
    print("Classificação: Recuperação")
else:
    print("Classificação: Reprovado")

