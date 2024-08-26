import os
os.system("cls || clear")
#declaração de variaveis
#solicitação
for i in range(4):
    nota=float(input("Digite a sua nota:"))   
#calculos
soma=float(nota+nota+nota+nota)
media=float(soma/4)
#exinbindo
print(f"Sua media: {media}")