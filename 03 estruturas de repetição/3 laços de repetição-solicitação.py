import os
os.system("cls || clear")
#declaração de variaveis
soma=0
#solicitação
for i in range(5):
    nota=int(input("Digite a nota:"))
    soma= soma + nota
#exibindo
print(f"Soma: {soma}")