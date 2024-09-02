import os
os.system("cls || clear")
contador=0
while True:
    numero=int(input("Insira um numero negativo(-):"))
    contador+=1
    print(f"Quantidade de numeros inseridos:{contador}")
    if numero>=0:
        print("Fim")
        break