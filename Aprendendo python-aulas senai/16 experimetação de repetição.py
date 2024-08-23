import os
os.system("cls || clear")
#solicitação
numero=float(input("Digite um numero: "))
#calculos
#primeiro teste
for i in range(1,11):
    print(f"{1}+{i}={1+i}")
print("Tabuada de multplicação.")
for i in range(1,11):
    print(f"{numero}*{i}={numero*i}")
print("Tabuada de subtração.")
for i in range(1,11):
    print(f"{numero}-{i}={numero-i}")
#mostrando ao usuario