num = float(input("Digite um número: "))

parte_inteira = int(num)
parte_decimal = num - parte_inteira

print(f"Parte inteira: {parte_inteira}")
print(f"Parte decimal: {parte_decimal:.2f}")

if parte_decimal > parte_inteira:
    print("A parte decimal é maior que a parte inteira.")
else:
    print("A parte decimal NÃO é maior que a parte inteira.")