import os
os.system("cls || clear")
pares=0
impares=0
soma=0
contador1=0
contador2=0
#solicitação
while True:
    for i in range (3):
        numeros=int(input("Digite um numero:"))
        contador1+=1
    if numeros % 2==0:
       pares= pares+pares
       soma=pares+pares
    if numeros % 2==1:
        impares=impares+1
        soma=impares+impares
    else:break
print(f"A soma:{soma}")
print(f"numeros pares:{pares}")
print(f"numeros impares:{impares}")
print(f"Quantidade de numeros insridos(pares):{contador1}")
