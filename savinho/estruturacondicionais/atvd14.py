salário = float(input("Digite o salário do funcionário: "))
if salário <= 1500:
    aumento = salário * 0.20
    novo_salário = salário + aumento
    print(f"O novo salário com aumento de 20% é: R${novo_salário:.2f}")
else:
    if salário <= 3000:
        aumento = salário * 0.15    
        novo_salário = salário + aumento
        print(f"O novo salário com aumento de 15% é: R${novo_salário:.2f}")
    else:
        if salário >= 5000:
            aumento = salário * 0.10
            novo_salário = salário + aumento
            print(f"O novo salário com aumento de 10% é: R${novo_salário:.2f}")