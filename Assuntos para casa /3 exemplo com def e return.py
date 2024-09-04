import os
os.system("cls|| clear")
#função com return
def descontos_salario(salario_bruto):
    vale_transporte=200
    vale_refeicao=100
    plano_saude=300

    resultado=salario_bruto-(vale_transporte+vale_refeicao+plano_saude)
    return resultado

salario_bruto=float(input("Digite seu salario:"))
salario_liquido=descontos_salario(salario_bruto)
print(f"salário líquido:{salario_liquido}")