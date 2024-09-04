while True:
    try:
        horas_usuario = float(input("Digite a quantidade de horas que você deseja estudar (em formato decimal, por exemplo, 18.5): "))
        if horas_usuario <= 0:
            raise ValueError("A meta deve ser um número positivo.")
        break
    except ValueError as e:
        print(f"Entrada inválida: {e}. Por favor, insira um número válido.")

horas = 0.0

# Calculos e verificação
while horas < horas_usuario:
    while True:
        try:
            horas1 = float(input("Digite o número de horas estudadas: "))
            if horas1 < 0:
                raise ValueError("O número de horas estudadas deve ser um valor positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, insira um número válido.")
    
    horas += horas1
    if horas < horas_usuario:
        print(f"Total de horas estudadas até agora: {horas:.2f} horas. Ainda faltam {horas_usuario - horas:.2f} horas para atingir a meta.")

# Calcula e exibe o resultado final
excedente = horas - horas_usuario
print(f"\nParabéns! Você atingiu a meta de {horas_usuario:.2f} horas de estudo.")
print(f"Total de horas estudadas: {horas:.2f} horas.")
if excedente > 0:
    print(f"Você excedeu a meta em {excedente:.2f} horas.")
else:
    print("Você atingiu exatamente sua meta de horas de estudo.")