import os 
os.system("cls || clear")
pares=0
impares=0
for i in range(5):
 numero=int(input("Digite um numero:"))
 if numero % 2==0:
    pares= pares +1
 else:
    impares= impares+1
#calculo e verificação(exibindo?)
print(f"Numeros pares:{pares}")
print(f"Numeros impares:{impares}")

