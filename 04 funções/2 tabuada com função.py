import os 
os.system("cls || clear")
#processamento
def mostrar_tabuada(numero,i):
    return f"{numero}*{i}={numero*i}"

#solicitação
numero=int(input("Digite um numero:"))


#exibição de dados
for i in range(11):
        print(mostrar_tabuada(numero,i))