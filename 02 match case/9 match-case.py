import os 
os.system("cls || clear")#limpa tela
#Solicitação 
print("""
1- cadastrar usuario
2- excluir usuario
3- sair do sistema
      """)
opcao=int(input("Digite a sua opção: "))
#Exibindo ao usuario
match(opcao):
    case 1:
        print(f"Opção de cadastrar usuario.")
    case 2:
        print(f"Opção de excluir usuario.")
    case 3:
        print(f"Opção de sair do sistema.")
    case _:
        print(f"Opção invalida!")