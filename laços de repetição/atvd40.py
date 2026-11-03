numero = int(input("Digite um número inteiro: "))

print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print(bin(numero))
elif opcao == "2":
    print(oct(numero))
elif opcao == "3":
    print(hex(numero))
else:
    print("Opção inválida!")