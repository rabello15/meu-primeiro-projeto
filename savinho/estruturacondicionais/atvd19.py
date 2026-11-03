hora = float(input("Digite a hora: "))
minuto = float(input("Digite o minuto: "))  
if (hora >=8 and hora <= 18) and (minuto >= 0 and minuto <= 59):
    print("está em horario comercial.")
else:
    print("fora do horario comercial.")    