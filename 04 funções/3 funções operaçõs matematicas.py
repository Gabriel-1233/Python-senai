import os 
os.system("cls || clear")
#funções
def operacao_adicao(numero1,numero2):
    adicao=numero1 +numero2
    return adicao
def operacao_subtracao(numero1,numero2):
    subtracao=numero1-numero2
    return subtracao
def operacao_multplicacao(numero1,numero2):
    multplicacao=numero1*numero2
    return multplicacao
def operacao_divisao(numero1,numero2):
    divisao=numero1/numero2
    return divisao
#perguntado ao usuario
numero1=float(input("Digite um numero:"))
numero2=float(input("Digite um numero:"))
#limpar as perguntas
os.system("cls || clear")
adicao=operacao_adicao(numero1,numero2)
subtracao=operacao_subtracao(numero1,numero2)
multiplicacao=operacao_multplicacao(numero1,numero2)
divisao=operacao_divisao(numero1,numero2)
#Exibindo ao usuario
print(f"A Soma dos numeros é:{adicao}")
print(f"A subtração dos numeros é:{subtracao}")
print(f"A Multplicação dos numeros é:{multiplicacao}")
print(f"A Divisão dos numeros é:{divisao}")