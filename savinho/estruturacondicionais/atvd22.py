x1 = float(input("Digite o x do ponto 1: "))
y1 = float(input("Digite o y do ponto 1: "))
x2 = float(input("Digite o x do ponto 2: "))
y2 = float(input("Digite o y do ponto 2: "))
x3 = float(input("Digite o x do ponto 3: "))
y3 = float(input("Digite o y do ponto 3: "))

resultado = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
if resultado == 0:
    print("Os pontos estão alinhados.")
else:
    print("Os pontos não estão alinhados.")