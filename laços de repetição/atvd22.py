idades = []

for i in range(5):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

media = sum(idades) / 5

print("Média:", media)
print("Idades acima da média:")

for idade in idades:
    if idade > media:
        print(idade)