"""
Escreva um algoritimo que solicite duas notas para um aluno.
Caso seja menor que 0 ou mair que 10, mostre a pergunta novamente.
Calcule e mostre a média aritimética do aluno.    

"""
import os
os.system("cls || clear")
#Declaração
nota1=0
nota2=0
#solicitação
while True:
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    media=float(nota1+nota2)/2
    if (nota1>10 or nota1<0) or (nota2>10 or nota2<0):
       print("Digite novamente as notas")
    else:break
print(f"Primeira nota:{nota1}")
print(f"Segunda nota:{nota2}")
print(f"A media do aluno:{media}")