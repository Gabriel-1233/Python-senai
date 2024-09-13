import os
os.system("cls || clear")
lista_numeros=[]

while len(lista_numeros)<6:
        try:
            numero=int(input("Digite um numero(par e positivo!):"))
            if (numero<0) or (numero % 2==0):
               lista_numeros.append(numero)
            else:
                  print("O valor deve ser positivo,par e inteiro!")
        except ValueError:
              print("O numero digitada não corresponde a nenhuma das caracterisaticas fundamentais!")
              print(lista_numeros)

for numero in reversed(lista_numeros):
    print(numero)