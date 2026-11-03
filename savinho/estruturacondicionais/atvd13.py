numero = float(input("Digite um número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e 5.")
elif numero % 3 == 0:       
    print("O número é divisível por 3.")
elif numero % 5 == 0:
    print("O número é divisível por 5.")
else:
    print("O número não é divisível por 3 nem por 5.")  
