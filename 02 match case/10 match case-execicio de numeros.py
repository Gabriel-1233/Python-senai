import os
os.system("cls || clear")#limpa tela
#solicitacao
numero1=float(input(f"Digite o primeiro numero: "))
numero2=float(input(f"Digite o segundo numero: "))
print("""
Escolha uma forma de operação!
1- soma
2- subtração
3- multplicação
4- divisão
       """)
opcao=float(input(f"Digite a forma de operação: "))
#calculos
soma=numero2+numero1
multplicacao=numero1*numero2
divisao=numero1/numero2
subtracao=numero1-numero2
#segunda parte
match(opcao):
    case 1:
        print(f"Primeiro numero: {numero1}")
        print(f"Segundo numero: {numero2}")
        print(f"Você escolheu está forma de operação, aqui está o resultado: {soma}")
    case 2:
        print(f"Primeiro numero: {numero1}")
        print(f"Segundo numero: {numero2}")
        print(f"Você escolheu está forma de operação, aqui está o resultado: {subtracao}")
    case 3:
        print(f"Primeiro numero: {numero1}")
        print(f"Segundo numero: {numero2}")
        print(f"Você escolheu está forma de operação, aqui está o resultado: {multplicacao}")
    case 4:
        print(f"Primeiro numero: {numero1}")
        print(f"Segundo numero: {numero2}")
        print(f"Você escolheu está forma de operação, aqui está o resultado: {divisao}")
    case _:
        print(f"Você escolheu uma opção inesistente!")

    

    

