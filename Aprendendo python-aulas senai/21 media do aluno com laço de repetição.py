import os
os.system("cls || clear")
#solicitação
for i in range(3):
   notas=float(input("Digite sua nota:"))
#calculos e variaveis
soma=float(notas+notas+notas)
media=soma/3
#exibindo
print(f"Sua media: {media}")
if media>=7:
   print("Você foi aprovado!")
if media>=4 and media<7:
   print("Você vai para recuperação!")
else:
   print("Você foi reprovado!")
