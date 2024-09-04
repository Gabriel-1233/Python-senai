def main():
    soma_impares = 0
    contagem_impares = 0
    
    print("Insira números inteiros até que a soma dos números ímpares inseridos seja maior que 200.")

    while soma_impares <= 200:
        while True:
            try:
                numero = int(input("Digite um número inteiro: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
        
        if numero % 2 != 0:
            soma_impares += numero
            contagem_impares += 1
            print(f"Total de números ímpares inseridos até agora: {contagem_impares}")
            print(f"Soma dos números ímpares inseridos até agora: {soma_impares}")
        else:
            print(f"O número {numero} é par e não é adicionado à soma dos ímpares.")

    print("\nMeta atingida!")
    print(f"Total de números ímpares inseridos: {contagem_impares}")
    print(f"Soma total dos números ímpares: {soma_impares}")

# Executa o programa
main()
