import os
os.system("cls || clear")
#declaração
soma=0
contador=0
#solicitação
while True:
    nota=float(input("Digite uma nota:"))
    contador+=1
    soma+=nota
    resposta=input("Deseja inserir mais uma nota?")
    resposta=resposta.upper()#converter a variavel em maiúsculo
    if resposta=="N":
        break
media=soma/contador
print(f"Média:{media}")
    