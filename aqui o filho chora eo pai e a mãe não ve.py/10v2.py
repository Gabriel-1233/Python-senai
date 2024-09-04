import os
os.system("cls || clear")
#solicitação
total_calorias=0
soma=0
while total_calorias<=2000:
       calorias=int(input("Digite o numero de calorias consumidas:"))
       if calorias<0:
            print("Entrada invalida.Por favor, insira outro valor.")
       total_calorias+=calorias
execesso=total_calorias-2000
print(f"\ntotal de calorias:{total_calorias:.2f}")   
print(f"excesso de calorias:{execesso:.2f}")   
