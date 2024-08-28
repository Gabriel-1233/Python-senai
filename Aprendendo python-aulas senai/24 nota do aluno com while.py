import os
os.system("cls || clear")
#solicitação
nota=float(input("Digite sua nota: "))
#verificações 
while nota<0 or nota>10:
    print("A nota deve ser maior ou igual a zero e menor igual a 10.")
    nota=float(input("DIgite uma nota: "))
#exibindo
print(f"Nota:{nota}")