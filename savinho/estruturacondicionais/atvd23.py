num = int(input("Digite um número de 5 dígitos: "))
d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10   

if d1 == d5 and d2 == d4:
    print(f"O número {num} é palíndromo.")
else:
    print(f"O número {num} não é palíndromo.")