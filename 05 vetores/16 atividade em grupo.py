import os 
os.system("cls || clear")

#funções
def limpar_terminal():
    import os 
    os.system("cls || clear")

def verificador_impar_par(lista_numero1):
    quantidade_impares = 0
    soma_impares = 0
    soma_pares = 0
    quantidade_pares = 0
    lista_pares = []
    lista_impar=[]
    for numero1 in lista_numero1:
        if numero1 % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero1
            lista_pares.append(numero1)
        else:
            quantidade_impares += 1
            soma_impares += 1
            lista_impar.append(numero1)
    return quantidade_pares,quantidade_impares

def verificacao_positivos(lista_numero1):
    contador_positivo=0
    contador_negativo=0
    for numeros in lista_numero1:
        if numeros>0: 
            contador_positivo+=1
        else: 
            contador_negativo+=1

    return contador_positivo,contador_negativo

def verificando_maior(lista_numero1):
    maior_numero=max(lista_numero1)
    return maior_numero

def verificando_menor(lista_numero1):
    menor_numero=min(lista_numero1)
    return menor_numero

def verificador_media_impar_par(lista_numero1):
    quantidade_impares = 0
    soma_impares = 0
    soma_pares = 0
    quantidade_pares = 0
    for numero1 in lista_numero1:
        if numero1 % 2 == 0:
            quantidade_pares+=1
            soma_pares+=numero1
            media_par=soma_pares/quantidade_pares
        elif numero1 % 2!=0:
            quantidade_impares+=1
            soma_impares+=numero1
            media_impar=soma_impares/quantidade_impares

    return media_par,media_impar

def verificador_media(lista_numero1):
    soma_geral = 0
    for numero1 in lista_numero1:
        soma_geral = numero1+numero1+numero1+numero1+numero1
        media_geral=soma_geral/QUANTIDADE
    return media_geral

#variaveis(constantes)
lista_numero1=[]
QUANTIDADE=5

#entrada
for i in range(QUANTIDADE):
    numeros=int(input(f"Digite {i+1}º numero:"))
    lista_numero1.append(numeros)
    limpar_terminal()

#processamento
contador_par,contador_impar=verificador_impar_par(lista_numero1)
contador_positivo,contador_negativo=verificacao_positivos(lista_numero1)
media_par,media_impar=verificador_media_impar_par(lista_numero1)
maior_numero = verificando_maior(lista_numero1)  
menor_numero=verificando_menor(lista_numero1)
media_geral=verificador_media(lista_numero1)

#saida
limpar_terminal()
print(f"A quantidade de numeros digitados:{QUANTIDADE}")
for i, numero in enumerate (lista_numero1):
    print(f"{i+1}º número:{numero}")
print(f"Pares: {contador_par}")
print(f"Ímpares: {contador_impar}")
print(f"Positivo: {contador_positivo}")
print(f"Negativo: {contador_negativo}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Media dos numeros pares: {media_par}")
print(f"Media dos numeros impares: {media_impar}")
print(f"Media dos numeros: {media_geral}")
for numero in reversed(lista_numero1):
        print(f"Números na ordem inversa: {numero}")
