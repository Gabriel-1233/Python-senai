import os
os.system("cls || clear")#limpa tela
#solicitacao
print("""
1-Janeiro
2-Fevereiro
3-Março
4-Abril
5-Maio
6-Junho
7-Julho
8-Agosto
9-Setembro
10-Outubro
11-Novembro
12-Dezembro
      """)
opcao=int(input("Digite o numero correspondente ao mês:"))
#mostrando ao usuario
match(opcao):
    case 1:
        print("O mês escolhido foi Janeiro,parabens!")
    case 2:
        print("O mês escolhido foi Fevereiro,parabens!")
    case 3:
        print("O mês escolhido foi Março,parabens!")
    case 4:
        print("O mês escolhido foi Abril,parabens!")
    case 5:
        print("O mês escolhido foi Maio,parabens!")
    case 6:
        print("O mês escolhido foi Junho,parabens!")
    case 7:
        print("O mês escolhido foi Julho,parabens!")
    case 8:
        print("O mês escolhido foi Agosto,parabens!")
    case 9:
        print("O mês escolhido foi Setembro,parabens!")
    case 10:
        print("O mês escolhido foi Outubro,parabens!")
    case 11:
        print("O mês escolhido foi Novembro,parabens!")
    case 12:
        print("O mês escolhido foi Dezembro,parabens!")
    case _:
        print("O numero escolhido não existe neste calendadario!")
        print("---FIM---")
if opcao<=12 and opcao>=1:
        print("Do ano de 2024!")
