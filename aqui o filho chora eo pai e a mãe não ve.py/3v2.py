import os
os.system("cls || clear")
numero_inicial=10
numero=0
contador=0
multplicacao=numero_inicial*numero
while True:
    if multplicacao<100:
        numero=int(input("Digite um numero:"))
        multplicacao=numero_inicial*numero
        contador+=1
    else:
        multplicacao=numero_inicial*numero
        print(f"Multiplicação:{multplicacao}")
        print(f"Numero de tentativas:{contador}")
        break
