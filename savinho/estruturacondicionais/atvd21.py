numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

q1 =(numero1 ** 0.5) % 1 == 0
q2 =(numero2 ** 0.5) % 1 == 0
q3 =(numero3 ** 0.5) % 1 == 0
q4 =(numero4 ** 0.5) % 1 == 0   

if q1 or q2 or q3 or q4:
    print("Pelo menos um dos números é um quadrado perfeito.")
else:
    print("Nenhum dos números é um quadrado perfeito.")