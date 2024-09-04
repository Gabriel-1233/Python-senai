import os
os.system("cls || clear")
#solicitação
nome1=str(input("Digite seu nome: "))
senha1=str(input("Digite a senha que você usara: "))
#Exibindo ao usuario.
while True:
  nome2=str(input("Digite seu login: "))
  senha2=str(input("Digite sua senha: "))

  if nome2==nome1 and senha2==senha1:
      print(f"Bem-vindo!")
      break
  if senha2!=senha1 or nome2!=nome1:
    print(f"Tente novamente!")
    print("Seu login ou senha estão errados")
