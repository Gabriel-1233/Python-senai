import os
os.system("cls || clear")
QUANTIDADE=5
vetor=[]

for i in range(QUANTIDADE):
    valor=int(input("Digite um numero:"))
    if valor<0:
        valor=0
        vetor.append(valor)
    else:
        vetor.append(valor)
for numero in vetor:
    print(f"Valor:{numero}")