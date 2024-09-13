import os
os.system("cls || clear")

#ENTRADA
lista_notas=[]
for i in range(3):
    notas=float(input("Digite uma nota:"))
    lista_notas.append(notas)

#SAIDA 
for notas in lista_notas:
    print(f"Nota:{notas}")