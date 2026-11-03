a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print('O triângulo é retângulo.')
    else:
        print('O triângulo não é retângulo.')
else:
    print('Os valores fornecidos não formam um triângulo.')    