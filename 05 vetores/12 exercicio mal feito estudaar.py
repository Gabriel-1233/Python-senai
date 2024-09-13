import os
os.system("cls || clear")
lista_numeros=[]
lista_atualizada=[]
def verificação_valores(lista_numeros):
    if (numero>0) or (numero % 2==0):
        
     lista_numeros.append(numero)
    
    return lista_numeros
while True:
  for i in range(6):
      numero=int(input("Digite um numero(par e positivo!):"))
  if (numero<0) or (numero % 2==1):
     print("Digite novamente!")
  elif (numero>0) and (numero % 2==0):
     lista_numeros.append(numero)
     break
for numero in reversed(lista_numeros):
   print(verificação_valores(lista_numeros))