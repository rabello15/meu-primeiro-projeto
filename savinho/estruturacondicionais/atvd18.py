dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
if(mes == 1 and 1 <= dia <= 31) or \
     (mes == 2 and 1 <= dia <= 29) or \
     (mes == 3 and 1 <= dia <= 31) or \
     (mes == 4 and 1 <= dia <= 30) or \
     (mes == 5 and 1 <= dia <= 31) or \
     (mes == 6 and 1 <= dia <= 30) or \
     (mes == 7 and 1 <= dia <= 31) or \
     (mes == 8 and 1 <= dia <= 31) or \
     (mes == 9 and 1 <= dia <= 30) or \
     (mes == 10 and 1 <= dia <= 31) or \
     (mes == 11 and 1 <= dia <= 30) or \
     (mes == 12 and 1 <= dia <= 31):
    print(f"A data {dia}/{mes}/{ano} é válida.")
else:
    print(f"A data {dia}/{mes}/{ano} é inválida.")  