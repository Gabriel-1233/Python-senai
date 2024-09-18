#Desculpe professor estar enviando a atividade pontuda muito tempo depois 
# eu tinha passado muito mau,tive dores pelo
# corpo,febre,,tosse e dificuldade em respirar.
# eu adimito aqui que fiz essa atividade com a ajuda de inteligencciass artificias.
# tambem tenho como comprovar que esses dias eu realmente estava mau.
import os
os.system("cls || clear")
# solicitando dados
numeros = []
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)
os.system("cls || clear")
# variaveis
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0

# maior e menor números com valores extremos
maior_numero = float('-inf')
menor_numero = float('inf')

# calculo e verificacao
for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1

    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)

    soma_geral += numero

# medias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# números na ordem inversa
numeros_invertidos = numeros[::-1]
os.system("cls || clear")
# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")
