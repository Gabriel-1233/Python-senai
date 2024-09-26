import os
from dataclasses import dataclass
os.system("cls || clear")

#Estrutura de dados.
@dataclass
class Cliente:
    nome:str
    sobrenome:str
    idade:int
    peso:float
    altura:float

#Constante e lista.
QUANTIDADE_ALUNOS=2
lista_alunos=[]

#Solicitando dados ao usuario.
print("\n===Solicitando dados aos alunos ===")
for i in range(QUANTIDADE_ALUNOS):
    aluno= Cliente(
        nome=input("Digite seu nome:"),
        sobrenome=input("Digite seu sobrenome:"),
        idade=int(input("Digite sua idade:")),
        peso=float(input("Digite seu peso:")),
        altura=float(input("Digite sua altura:"))

    )
    lista_alunos.append(aluno)

#Exbindo dados para o usuario
print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_alunos:
    print(f"Nome:{aluno.nome}")
    print(f"Idade:{aluno.sobrenome}")
    print(f"Idade:{aluno.idade}")
    print(f"Idade:{aluno.peso}")
    print(f"Idade:{aluno.altura}")

#nome do arquivo e seu processamento.
nome_do_arquivo="carteira_de_clientes.txt"
with open(nome_do_arquivo, "a") as arquivos_alunos:
    for aluno in lista_alunos:
        arquivos_alunos.write(f"{aluno.nome}, {aluno.sobrenome}, {aluno.idade}, {aluno.peso}, {aluno.altura}\n")

#fechar arquivo, para poder parar de utilizar poder de computação.
arquivos_alunos.close()

#segunda crud.
print("\n===Dados dos alunos salvo com sucesso!===")
#limpando a lista de alunos.
lista_alunos=[]
#Lendo dados de um arquivo.
print("\n===Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome,sobrenome,idade,peso,altura =linha.strip().split(",")
        lista_alunos.append(Cliente (nome=nome, sobrenome=sobrenome, idade=int(idade), peso=float(peso), altura=float(altura) ))

#fechar arquivo,para poder parar de utilizar poder de computação.
arquivos_alunos.close()

print("\n=== Exbindo dados dos alunos do arquivo ===")
for aluno in lista_alunos:
    print(f"Nome:{aluno.nome}")
    print(f"Idade:{aluno.sobrenome}")
    print(f"Idade:{aluno.idade}")
    print(f"Idade:{aluno.peso}")
    print(f"Idade:{aluno.altura}")