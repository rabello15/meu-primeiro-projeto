a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Os valores podem formar um equilátero.")
    else:
        print("Os valores podem formar um isósceles.")
elif a == b or a == c or b == c:
    print("Os valores podem formar um isósceles.")
else:
    print("Os valores podem formar um escaleno.")
