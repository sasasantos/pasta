import os

os.system("cls")
def limpar_tela():
    os.system("cls")

def obter_numero(mensagem):
     while True:
        try:
            return int(input(mensagem))
        except Exception as erro:
            print(f"Acontecdeu um erro: {erro}")
            print("Digite um valor inválido. Tente novamente.")

print("----------------------------------------------------------------------")
print("------------------------- PROJETO SOMA -------------------------------")
print("----------------------------------------------------------------------")

try:

    valor01 = obter_numero("Digite o primeiro número: ")
    valor02 = obter_numero("Digite o segundo número: ")

    total = valor01 + valor02
    print(f"O resultado da soma é: {total}")

except:
    print("Digite apenas números inteiros!")


input("Pressione a tecla <Enter> para continuar...")