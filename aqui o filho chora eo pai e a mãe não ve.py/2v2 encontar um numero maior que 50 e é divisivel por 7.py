import os
os.system("cls || clear")
#solicitação
while True:
    numero=float(input("Digite um numero que seja maior que cinquenta:"))
    divisao=numero/7==0
    if numero>50 and numero % 7==0:
         divisao=numero/7==0
         print(f"Numero:{numero}")
         print(f"Numero divisivel:{divisao}")
         break
    if numero<50:
         print("O numero digitado é menor que cinquenta!")     
         numero=float(input("Digite um numero que seja maior que cinquenta:"))
         if numero>50 and numero % 7==0:
                print(f"Numero:{numero}")
                print(f"Numero divisivel:{divisao}")
                break
    else:
         print("Tem alguma coisa errada")
         break