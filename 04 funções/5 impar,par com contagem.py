import os 
os.system("cls || clear")
def verificar_pares_impares():
    pares=0
    impares=0

    for i in range(6):
        numero=int(input("Digite um numero:"))

        if numero % 2==0:
            pares+=1
        else:
            impares+=1
    print(f"\nQuantidade de numeros pares:{pares}")
    print(f"\nQuantidade de numeros impares:{impares}")
verificar_pares_impares()