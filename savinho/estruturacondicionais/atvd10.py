altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em kg: "))    

imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
elif imc <= 24.9:
    print(f"Seu IMC é {imc:.2f}. Você está com o peso normal.")
elif imc <= 29.9:
    print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")
else:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade.")