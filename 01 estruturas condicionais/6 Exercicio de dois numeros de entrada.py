import os
os.system("cls || clear")
#Solicicao de dados
numero1=float(input("Digite o primeiro numero:"))
numero2=float(input("Digite o sgundo numero:"))
#verificacao
soma=numero1+numero2
subtracao=numero1-numero2
multplicacao=numero1*numero2
divisao=numero1/numero2
#Exibindo dados
print(f"Primeiro numero: {numero1}")
print(f"Segundo numero: {numero2}")
print(f"Resultado da soma: {soma}")
print(f"Resultado da divisao: {divisao}")
print(f"Resultado da multplicacao: {multplicacao}")
if numero1>numero2:
   print("O numero 1 é o maior valor!")
if numero2>numero1:
   print("O numero 2 é o maior valor!")
if numero1==numero2:
   print("Os numeros são iguais!")
