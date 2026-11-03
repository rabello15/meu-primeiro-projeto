capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa mensal (%): "))
meses = int(input("Digite a quantidade de meses: "))

saldo = capital

for mes in range(1, meses + 1):
    saldo = saldo * (1 + taxa / 100)
    print("Mês", mes, "- Saldo: R$", round(saldo, 2))

print("Saldo final: R$", round(saldo, 2))