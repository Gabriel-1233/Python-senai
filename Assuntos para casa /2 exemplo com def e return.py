import os
os.system("cls || clear")
#função com retorno.
def somar(n1,n2):
    soma = n1+n2
    return soma

numero_1=int(input("Digite o primeiro numero:"))
numero_2=int(input("Digite o segundo numero:"))
soma=somar(numero_1,numero_2)
print(f"Soma:{soma}")
