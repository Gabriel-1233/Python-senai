import os 
os.system("cls || clear")#limpa tela
#solicitação de dados
idade=int(input("Digite sua idade: "))
#calculos
if idade>=18 and idade<=65:
   print(f"Você é obrigado a votar!")
else:
   print(f"Você não é obrigado a votar!")
#exibindo dados 