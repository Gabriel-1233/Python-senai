import os
os.system("cls || clear")
#solicitação
horas_usuario=float(input("Digite a quantidade de horas,mas de forma inteira(18,24,6 e etc):"))
horas=0.0
#calculos e verificação
while horas<horas_usuario:
    horas1 = float(input("Digite o número de horas estudadas: "))
    horas += horas1
    if horas < horas_usuario:
        print(f"Total de horas estudadas até agora: {horas:.2f} horas. Ainda faltam {horas_usuario - horas:.2f} horas para atingir a meta.")
    excedente = horas - horas_usuario
    print(f"Parabéns! Você atingiu a meta de {horas_usuario:.2f} horas de estudo.")   