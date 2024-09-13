import os
os.system("cls || clear")
#declaração
soma=0
contador=0
#solicitação
while True:
    nota1=float(input("Digite uma nota:"))
    if (nota1>10 or nota1<0):
      print("Digite novamente!")
    else:break
print("""
1-O usuario deseja digitar outra nota?
2-Não!
          """)
opcao=int(input("Digite a sua opção:"))
match(opcao):
    case 1:
      for i in range(1):
        numero_de_notas=2
        nota2=float(input("Digite a nota:"))
        soma=nota1+nota2
        media=soma/2
        print(f"O numero de notas é:{numero_de_notas}")
        print(f"Media:{media}")
    case 2:
      numero_de_notas=1
      print(f"O numero de notas é:{numero_de_notas}")
      media=nota1/2
      print(f"Media:{media}")
      print("Obrigada por usar nosso site!")
    case _:
      print("Você escolheu um opção inesistente")