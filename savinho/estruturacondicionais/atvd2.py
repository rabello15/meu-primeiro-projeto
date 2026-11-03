# Pede o número APENAS UMA VEZ
número = int(input("Digite o número: "))

# 1. Teste de Par / Ímpar
if número % 2 == 0:
    print(f"O número {número} é par.")
else:
    print(f"O número {número} é impar.")

# 2. Teste de Positivo / Negativo / Zero (usa a mesma variável 'número')
if número > 0:
    print(f"O número {número} é positivo.")
elif número < 0:
    print(f"O número {número} é negativo.")
else:
    print("O número é zero.")