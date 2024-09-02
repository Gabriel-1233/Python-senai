

import os
os.system("cls || clear")
#Declaração
nota1=0
nota2=0
nota3=0
notas=0
#solicitação
while True:
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    nota3=float(input("Digite a sua terceria nota:"))
    media=float(nota1+nota2+nota3)/3
    if (nota1>10 or nota1<0) or (nota2>10 or nota2<0) or (nota3>10 or nota3<0):
       print("Digite novamente as notas")
    else:break
print("""  
1- O usuario deseja inserir outra nota?
2- Não.
3- O usuario deseja ver o numero de notas e a media?
      """)
opcao=int(input("Digite o numero correspondente a sua opção: "))
#if opcao==1 or opcao==2:
match(opcao):
         case 1: 
              for i in range(1):
                  nota_1=float(input("Digite a nota:"))
                  media=float(nota1+nota2+nota3+nota_1)/4
                  if (nota_1>10 or nota_1<0):
                     print("Digite novamente")
                  elif nota_1<=10 or nota_1<0:
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
                   print("Obriaga por usar nosso site!")
                  else:break
         case 2:
              media=float(nota1+nota2+nota3)/3
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
              print("Obriaga por usar nosso site!")
         case _:
              print("Você escolheu uma opção inesistente!")
              print("Obriaga por usar nosso site!")
