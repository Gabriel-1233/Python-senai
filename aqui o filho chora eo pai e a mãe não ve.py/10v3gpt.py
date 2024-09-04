def registrar_calorias():
    total_calorias = 0
    
    print("Registro de Calorias")
    print("-------------------")
    
    while total_calorias <= 2000:
        try:
            calorias = float(input("Digite o número de calorias consumidas na refeição: "))
            
            if calorias < 0:
                print("O número de calorias não pode ser negativo. Tente novamente.")
                continue
            
            total_calorias += calorias
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    
    excesso = total_calorias - 2000
    
    print("\nTotal de calorias consumidas: {:.2f}".format(total_calorias))
    print("Excesso de calorias: {:.2f}".format(excesso))

# Executar a função
registrar_calorias()
