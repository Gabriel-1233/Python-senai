import os
os.system("cls || clear")
#ENTRADA
QUANTIDADE=4
lista_notas=[]
for i in range(QUANTIDADE):
    notas=float(input("Digite uma nota:"))
    lista_notas.append(notas)
soma=sum(lista_notas)
media=soma/QUANTIDADE
os.system("cls || clear")
#SAIDA 
for notas in lista_notas:
    print(f"Nota:{notas}")
print(f"\nMedia:{media}")
if media>=7:
   print("Você foi aprovado!")
if media>=4 and media<7:
   print("Você vai para recuperação!")
else:
   print("Você foi reprovado!")