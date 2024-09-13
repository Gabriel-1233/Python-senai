import os
os.system("cls || clear")#Limpa tela
# if é igual a verdadeiro,falso ou se
# else é igual a senao
# and igual a e
#or é igaul a ou
#not é igual a negação
#Solicitação de dados.
nome1=str(input("Digite seu nome: "))
senha1=str(input("Digite a senha que você usara: "))

#Entrada do usuario.
nome2=str(input("Digite seu login: "))
senha2=str(input("Digite sua senha: "))

#Exibindo ao usuario.
if nome2==nome1 and senha2==senha1:
    print(f"Bem-vindo!")
else:
    print("Seu login ou senha estão errados")
if senha2!=senha1 or nome2!=nome1:
    print(f"Tente novamente!")

