ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")
    