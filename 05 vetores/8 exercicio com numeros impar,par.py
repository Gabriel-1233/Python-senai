import os
os.system("cls || clear")
#ENTRADA 
par=0
impar=0
QUANTIDADE=6
lista_numeros=[]
#calculos ou verificação
for i in range(QUANTIDADE):
    numero=float(input(f"Digite um numero:"))
    lista_numeros.append(numero)
    if numero % 2==0:
        par+=1
    else:
        impar+=1
os.system("cls || clear")
#saida
for numero in lista_numeros:
    print(f"\nNota:{numero}")
print(f"\nNumeros pares:{par}")  
print(f"\nNumeros impares:{impar}")  