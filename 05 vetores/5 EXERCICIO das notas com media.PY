import os
os.system("cls || clear")
#ENTRADA
QUANTIDADE=3
lista_notas=[]
for i in range(QUANTIDADE):
    notas=float(input("Digite uma nota:"))
    lista_notas.append(notas)
soma=sum(lista_notas)
media=soma/QUANTIDADE
#SAIDA 
for notas in lista_notas:
    print(f"Nota:{notas}")
print(f"Media:{media}")