h1 = int(input("hora 1: "))
m1 = int(input("minuto 1: "))

h2 = int(input("hora 2: "))
m2 = int(input("minuto 2: "))

total1 = h1 * 60 + m1
total2 = h2 * 60 + m2

if total1 < total2:
    print(f"o primeiro horário acontece primeiro.")
elif total2 < total1:
    print(f"o segundo horário acontece primeiro.")
else:
    print(f"os dois horários são iguais.")
