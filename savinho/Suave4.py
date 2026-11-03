nome = input("Qual é o nome do produto? ")
preço = float(input("Qual é o preço do produto? "))
quantidade = int(input("Qual é a quantidade do produto? "))
percentual_desconto = float(input("Qual é o percentual de desconto? "))
numero_parcelas = int(input("Qual é o número de parcelas? "))

valor_bruto = preço * quantidade
desconto = valor_bruto * (percentual_desconto / 100)
valor_final = valor_bruto - desconto
valor_parcela = valor_final / numero_parcelas

print(f"Nome do produto: {nome}")
print(f"Preço do produto: R$ {preço:.2f}")
print(f"Quantidade do produto: {quantidade}")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"Número de parcelas: {numero_parcelas}")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
print(f"Valor da parcela: R$ {valor_parcela:.2f}")









