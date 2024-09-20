import os
os.system("cls || clear")
#declaração
QUANTIDADE=5
pares=0
impares=0
negativos=0
positivos=0
#solicitação
for i in range(QUANTIDADE):
    numeros=int(input("Digite um numero:"))
    if numeros<0:
        negativos+=1
    else:
        positivos+=1
    if numeros % 2==0:
        pares+=1
    elif numeros % 2==1:
        impares+=1
os.system("cls || clear")
#exibindo
print(f"Quantidade de numeros positivos:{positivos}")
print(f"Quantidade de numeros negativos:{negativos}")
print(f"Quantidade de numeros pares:{pares}")
print(f"Quantidade de numeros impares:{impares}")