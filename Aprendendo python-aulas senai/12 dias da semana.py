import os
os.system("cls ||clear")#limpa tela
#solicitacao
print("""
---Dias da Semana---
1- Domingo
2- Segunda-feira
3- Terça-feira
4- Quarta-feira
5-¨Quinta-feira
6- Sexta-feira
7- Sabado
      """)
opcao=int(input("Digite o numero corespondente ao dia da semana: "))
match(opcao):
    case 1:
        print(f"Domingo.")
    case 2:
        print(f"Segunda-feira.")
    case 3:
        print(f"Terça-feira.")
    case 4:
        print(f"Quarta-feira.")
    case 5:
        print(f"Quinta-feira.")
    case 6:
        print(f"Sexta-feira.")
    case 7:
        print(f"Sabado.")
    case _:
        print(f"Você escolheu um dia da semana que não existe!, pelo menos neste calendario :).")
if opcao>=2 and opcao<=6:
    print(f"Feliz dia da semana!!!")
if opcao==1 or opcao==7:
    print(f"Feliz final de semana!!!")
    
    
    