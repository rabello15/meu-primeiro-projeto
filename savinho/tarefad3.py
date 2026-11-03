nome =input("Qual  o nome do funcionário? ")
salário = float(input("Qual é o salário do funcionário? "))
percentual_aumento = float(input("Qual é o percentual de desconto do INSS? "))
Percentual = float(input("Qual é o percentual de desconto do plano de saúde? "))

desconto_inss = salário * (percentual_aumento / 100)
desconto_plano_saude = salário * (Percentual / 100)
salário_liquido = salário - desconto_inss - desconto_plano_saude    
total = desconto_inss + desconto_plano_saude

print(f"\nFuncionário: {nome}")
print(f"Salário bruto: R$ {salário:.2f}")
print(f"Desconto do INSS: R$ {desconto_inss:.2f}")
print(f"Desconto do plano de saúde: R$ {desconto_plano_saude:.2f}")
print(f"Salário líquido: R$ {salário_liquido:.2f}")
