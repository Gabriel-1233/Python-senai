import os
os.system("cls || clear")
#solicitação
QUANTIDADE_NOTAS=2
soma=0
for i in range(QUANTIDADE_NOTAS):
   while True:
      nota=float(input(f"Digite {i+1} a nota: "))
      if nota>=0 and nota<=10:
        break 
      soma+=nota
media=soma/QUANTIDADE_NOTAS
print(f"Media:{media}")
