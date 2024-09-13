import os
os.system("cls || clear")
#ENTRADA 
QUANTIDADE=5
lista_numeros=[]

for i in range(QUANTIDADE):
    numero=float(input(f"Digite um numero:"))
    lista_numeros.append(numero)

#PROCESSAMENTO.
maior_numero=max(lista_numeros)
menor_numero=min(lista_numeros)

#saida
for numero in lista_numeros:
    print(f"Nota:{numero}")
print(f"\nMenor numero:{menor_numero}")  
print(f"\nMaior numero:{maior_numero}")  