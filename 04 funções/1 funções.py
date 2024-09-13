import os
os.system("cls || clear")
def calcular_media(numero1,numero2):
    soma=numero1+numero2
    media=soma/2
    return media
numero1=float(input("Digite o numero:"))
numero2=float(input("Digite o numero:"))
media=calcular_media(numero1,numero2)
print(f"A media é:{media}")