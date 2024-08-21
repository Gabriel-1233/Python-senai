import os 
os.system("cls || clear")#limpa tela
#solicitacao
print("""
---Prato---
1-Picanha R$25,00
2-Lasanha R$20,00
3-Strogonoff R$18,00
4-Bife Acebolado R$15,00
5-Pão com ovos R$5.00
 """)
opcao=float(input("Digite o numero do prato: "))
#valor dos pratos
picanha=25.00
Lasanha=20.00
Strogonoff=18.00
Bife_Acebolado=15.00
Pão_com_ovo=5.00
#exibindo ao usuario
match(opcao):
    case 1:
        print(f"--Picanha--")
        print(f"O prato que você escolheu custa: {picanha}")
    case 2:
        print(f"--Lasanha--")
        print(f"O preço do prato escolhido é: {Lasanha}")
    case 3:
        print(f"--Strogonoff--")
        print(f"O preço do prato escolhido é: {Strogonoff}")
    case 4:
        print(f"--Bife Acebolado--")
        print(f"O preço do prato escolhido é: {Bife_Acebolado}")
    case 5:
        print(f"--Pão com ovos--")
        print(f"O preço do prato escolhido é: {Pão_com_ovo}")
    case _:
        print(f"Você escolheu um opção inesistente!")

        