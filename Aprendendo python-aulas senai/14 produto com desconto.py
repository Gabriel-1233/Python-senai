import os
os.system("cls || clear")#limpa tela
#solicitacao
print("""
1-Pagamento a vista
2-Pagamento a prazo
      """)
opcao=int(input("Digite o numero corespondente a opção: "))
#verifiacao ou calculos
match(opcao):
    case 1:
        preco_produto=100
        desconto=preco_produto *0.10
        preco_final=preco_produto-desconto
        print(f"Preço do produto:{preco_produto}")
        print(f"Forma de pagamento: a vista")
        print(f"Valor do desconto: R${desconto}")
        print(f"Total a pagar: R${preco_final:.2f}")

    case 2:
        preco_produto=100
        parcelas=int(input("Digite a quantidade de parcelas: "))
        preco_parcelado=preco_produto/parcelas
        preco_final=preco_produto
        print(f"O preço do produto: {preco_produto}")
        print(f"Forma de pagamento: a prazo")
        print(f"O preço parcelado: {preco_parcelado:.2f}")
        print(f"Total a prazo:{preco_final:.2f}")

#mostrando ao usuario