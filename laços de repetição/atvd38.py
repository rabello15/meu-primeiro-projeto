soma_notas = 0
soma_pesos = 0

for i in range(3):
    nota = float(input("Digite a nota: "))
    peso = float(input("Digite o peso: "))

    soma_notas += nota * peso
    soma_pesos += peso

media = soma_notas / soma_pesos

print("Média ponderada:", media)