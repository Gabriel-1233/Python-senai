import os
os.system("cls || clear")
#solicitação de dados 
#upper é igual a tornar todas as letras em maiusculo
#lower é igaul a tornar todas as letras em minusculo
sexo=str(input("Digite seu sexo(M ou F): ")).upper()
altura=float(input("Digite a sua altura: "))
peso_ideal=0
#calculando
if sexo=="M" or sexo=="m":
      peso_ideal=(72.7 * altura)-58
      print(f"O seu peso ideal é: {peso_ideal:.3f}")
if sexo=="F" or sexo=="f":
      peso_ideal=(62.1 * altura)-44.7
      print(f"O seu peso ideal é: {peso_ideal:.3f}")
if sexo!="M" or sexo!="F":
      print("Digite seu sexo!")
print("===FIM===")
#exibindo ao usuario
print(f"Sexo: {sexo}")
print(f"Peso ideal: {peso_ideal:.3f}")
print(f"Altura: {altura}")