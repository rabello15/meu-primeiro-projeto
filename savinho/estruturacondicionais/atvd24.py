h1 = float(input(" hora1: "))
m1 = float(input(" minuto1: "))
s1 = float(input(" segundo1: "))

h2 = float(input(" hora2: "))
m2 = float(input(" minuto2: "))
s2 = float(input(" segundo2: "))

total1 = h1 * 3600 + m1 * 60 + s1
total2 = h2 * 3600 + m2 * 60 + s2   

if total1 > total2:
    print(f"o primeiro horário é o maior ({int(total1)} segundos).")
elif total2 > total1:
    print(f"o segundo horário é o maior ({int(total2)} segundos).")
else:
    print(f"os dois horários são iguais ({int(total1)} segundos).")