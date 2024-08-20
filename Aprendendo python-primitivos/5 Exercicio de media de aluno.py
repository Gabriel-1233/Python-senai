import os 
os.system("cls || clear")
#solicitacao de dados ao usuario
nome=str(input("Digite seu nome: "))
idade=int(input("Digite sua idade: "))
nota1=float(input("Digite a sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
nota3=float(input("Digite sua terceira nota: "))
#calculando
soma=float(nota1+nota2+nota3)
media=float(soma /3)
#exibindo dados
print(f"Nome: {nome}")
print(f"Idade: {idade} anos.")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Terceira nota: {nota3}")
print(f"Soma de todas as notas: {soma}")
print(f"A sua media: {media}")
if media >=7:
  print("Aprovado!")
else:
  print("Reprovado!")
print("---FIM---")
   