import os
os.system("cls || clear")
#solicitção
gastos_mensais=0
orcamento=float(input("Digite seu orçamento ou salario:"))
#calculando ou verificando
while True:
    for i in range(5):
      gastos_diario=float(input("\nDigite seu gasto diario:"))
      gastos_mensais+=gastos_diario
    if gastos_mensais==0:
        break
    gastos_mensais+=gastos_diario    
    if gastos_mensais>orcamento:
       exedente=gastos_mensais-orcamento
       print(f"Você gastou R${gastos_mensais:.2f}.")
    else:
       print(f"Você gastou R${gastos_mensais:.2f}.")