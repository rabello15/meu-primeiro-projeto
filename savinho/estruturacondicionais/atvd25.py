idade = float(input("Digite a idade: "))
tempodecontribuição = float(input("Digite o tempo de contribuição: ")) 
if idade >= 65 or tempodecontribuição >= 35:
    print("O funcionário pode se aposentar.")
else:
    print("O funcionário não pode se aposentar.")
     