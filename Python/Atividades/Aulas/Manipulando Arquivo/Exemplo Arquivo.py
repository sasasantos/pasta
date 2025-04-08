import os

os.system("cls")

print("----------------------------------------------------------------------")
print("--------------------- MANIPULAÇÃO DE DADOS ---------------------------")
print("----------------------------------------------------------------------")

arquivo = open("cotacao.txt", "w")

try:
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    with open("cotacao.txt", "w") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.close()
except:
    print("Erro ao manipular o arquivo")

input("Pressione <Enter> para continuar ...")