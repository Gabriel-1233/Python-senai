import os
os.system("cls || clear")
#declaração
QUANTIDADE=5
#funções
def verificar_numeros_pares(lista_de_numeros):
    pares=0
    for cada_numero in lista_de_numeros:
        if cada_numero % 2==0:
            pares+=1
    return pares
def verificar_numeros_impares(lista_de_numeros):
    impares=0
    for cada_numero in lista_de_numeros:
        if cada_numero % 2==1:
            impares+=1
    return impares
def verificar_numeros_negativos(lista_de_numeros):
    negativos=0
    for cada_numero in lista_de_numeros:
        if cada_numero<0:
            negativos+=1
    return negativos
def verificar_numeros_positivos(lista_de_numeros):
    positivos=0
    for cada_numero in lista_de_numeros:
        if cada_numero>0:
            positivos+=1
    return positivos

#solicitação
for i in range(QUANTIDADE):
    cada_numero=int(input(f"Digite o {i+1}º numero"))
    lista_de_numeros.append(cada_numero)

