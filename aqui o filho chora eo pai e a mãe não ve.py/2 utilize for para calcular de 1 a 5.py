import os 
os.system("cls || clear")
for i in range(0,6):
    numero=int(input("Digite um numero(digite de 1 a 5 nunca ultrapasse:( :"))
    soma=numero+i
    while True:
       if numero>5 or numero<0:
          print("Digite novamente!")
          break
       elif numero<=5 or numero>0:
          for i in range(0,6):
             soma=numero+i
             print(f"{numero}+{i}={numero+i}")
             print(f"Soma:{soma}")
          break
       else:break
   