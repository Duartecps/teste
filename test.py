h=int(input("Digite um número  "))
l=int(input("Digite outro número  "))
m=int(input("Digite outro número"))

total = h+l+m
total2 = h-l+m
total3 = h*l*m
total4 = h/l/m

pergunta=str(input("Qual operação você deseja realizar? Digite: soma, subtração, multiplicação ou divisão  "))
if pergunta == "soma":
    print(total)
elif pergunta == "subtração":
    print(total2)
elif pergunta == "multiplicação":
    print(total3)
elif pergunta == "divisão":
    print(total4)
else:
    print("erro)")