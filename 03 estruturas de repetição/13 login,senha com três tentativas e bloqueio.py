import os
os.system("cls || clear")
#solicitação
for i in range(1):
    login=str(input("Digite o seu login: "))
    senha=int(input("Digite sua senha: "))
    login_salvo=login
    senha_salva=senha
#verificação ou calculos
    for i in range(3):
        login2=str(input("Digite seu login: "))
        senha2=int(input("Digite sua senha: "))
        if (senha2!=senha_salva) or (login2!=login_salvo):
            print("Você foi bloqueado")
        else:
            print("Bem-vindo!")
            break
#exibindo
print("---FIM---")