import os
os.system("cls || clear")
numero_negativo=[]
numero_positivo=[]
QUANTIDADE=10
lista_numeros=[]

#processamento
for i in range(QUANTIDADE):
    numero=float(input(f"Digite um numero:"))
    lista_numeros.append(numero)
    if numero<0:
        numero_negativo.append(numero)
    else:
        numero_positivo.append(numero)
        
quantidade_negativos=len(numero_negativo)
soma_positivos=sum(numero_positivo)

os.system("cls || clear")
#saida
for numero in lista_numeros:
    print(f"Numero:{numero}")
print(f"Soma:{soma_positivos}")  
print(f"\nNumeros negativos:{quantidade_negativos}")