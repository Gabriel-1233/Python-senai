import os
os.system("cls || clear")
#declaração
contador=0
continua='s'
while continua=='s':
    print("Repetindo")
    contador+=1
#   contador=contador + 1
    continua=input("Tecle 's' se ddesejar continuar: ").strip().lower()
if contador==0:
    print("O bloco não foi repetido")
else:
    print(f"O bloco foi repetido:{contador} vezes")