a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a+b > c and a+c > b and b+c > a:

  if a == b and b == c:
   print("O triângulo é equilátero.")
  elif a == b or a == c or b == c:
   print("O triângulo é isósceles.")
  else:
   print("O triângulo é escaleno.")
else:
 print("Os valores fornecidos não formam um triângulo.")