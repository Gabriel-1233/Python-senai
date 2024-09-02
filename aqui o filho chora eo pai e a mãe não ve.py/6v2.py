import os
os.system("cls || clear")
nota1=0
nota2=0
nota3=0
#solicitação
while True:
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    nota3=float(input("Digite a sua terceria nota:"))
    media=float(nota1+nota2+nota3)/3
    if (nota1>10 or nota1<0) or (nota2>10 or nota2<0) or (nota3>10 or nota3<0):
       print("Digite novamente as notas")
    else:break
print(f"Primeira nota:{nota1}")
print(f"Segunda nota:{nota2}")
print(f"Terceira nota:{nota3}")
print(f"A media do aluno:{media:.2f}")
if media>=7 or media>=10:
       print("Aprovado")
elif media>=5 or media<=6.9:
        print("Recuperação")
elif media>5:
        print("Reprovado")
