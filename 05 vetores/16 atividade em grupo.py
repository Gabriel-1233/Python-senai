
import time
import os 
os.system("cls || clear")
def limpar_terminal():
    import os 
    os.system("cls || clear")

#funções

def verificacao_pares(lista_numero):
    contador_par=0
    lista_pares = []
    for numeros in lista_numero:
        if numeros % 2==0:
            contador_par+=1
            lista_pares.append(numeros)
    return contador_par, lista_pares

def verificacao_impares(lista_numero):
    contador_impar=0
    lista_impar = []
    for numeros in lista_numero:
        if numeros % 2==1:
            contador_impar+=1
            lista_impar.append(numeros)
    return contador_impar, lista_impar

def verificacao_positivos(lista_numero):
    contador_positivo=0
    for numeros in lista_numero:
        if numeros>0: 
            contador_positivo+=1
    return contador_positivo

def verificacao_negativos(lista_numero):
    contador_negativo=0
    for numeros in lista_numero:
        if numeros<0: 
            contador_negativo+=1
    return contador_negativo

def verificando_maior(lista_numero):
    maior_numero=max(lista_numero)
    return maior_numero

def verificando_menor(lista_numero):
    menor_numero=min(lista_numero)
    return menor_numero

def verificar_media_pares(lista_pares):
    lista_media_pares = []
    for numeros in lista_pares:
        lista_media_pares = []



#variaveis(constantes)
lista_numero=[]
QUANTIDADE=5

#entrada
for i in range(QUANTIDADE):
    numeros=int(input(f"Digite {i+1}º numero:"))
    lista_numero.append(numeros)
    limpar_terminal()

#processamento
contador_par, lista_par=verificacao_pares(lista_numero)
contador_impar,lista_impar=verificacao_impares(lista_numero)
contador_negativo =verificacao_negativos(lista_numero)
contador_positivo=verificacao_positivos(lista_numero)
maior_numero = verificando_maior(lista_numero)  
menor_numero=verificando_menor(lista_numero)

#saida
limpar_terminal()
print(f"A quantidade de numeros digitados:{QUANTIDADE}")
for i, numero in enumerate (lista_numero):
    print(f"{i+1}º número:{numero}")

print(f"Pares: {contador_par}")
print(f"Ímpares: {contador_impar}")
print(f"Positivo: {contador_positivo}")
print(f"Negativo: {contador_negativo}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
