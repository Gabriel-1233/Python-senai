"""
Crie um programa que solicite ao usuario seu login e uma senha.
O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.
"""
import os
os.system("cls || clear")
#declaração
#solicitação
for i in range(1):
    login=str(input("Digite seu login: "))
    senha=int(input("Digite sua senha: "))
    senha_salva=senha
    login_salvo=login
#entrada do usuario
    while True:
      login2=str(input("Digite seu login:"))
      senha2=int(input("Digite sua senha: "))
      if login2!=login_salvo and senha2!=senha_salva:
           print("A senha está errada repita!")
      else:break
print("Bem-Vindo!")