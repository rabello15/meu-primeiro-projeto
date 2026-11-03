a = 0
b = 0
c = 0

while True:
    voto = input("Vote em A, B, C ou digite fim: ").lower()

    if voto == "fim":
        break
    elif voto == "a":
        a += 1
    elif voto == "b":
        b += 1
    elif voto == "c":
        c += 1
    else:
        print("Voto inválido!")

print("Candidato A:", a)
print("Candidato B:", b)
print("Candidato C:", c)

if a > b and a > c:
    print("Vencedor: A")
elif b > a and b > c:
    print("Vencedor: B")
elif c > a and c > b:
    print("Vencedor: C")
else:
    print("Houve empate!")