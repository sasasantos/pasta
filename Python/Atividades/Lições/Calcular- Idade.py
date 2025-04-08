import os

os.system("cls")

print("Idade")

ano_atual = int(input("Digite o Ano Atual: "))

ano_nascimento = int(input("Digite o Ano de Nascimento: "))

Idade = (ano_atual - ano_nascimento)

os.system("cls")

print("Ano atual: " ,+ ano_atual)
print("Ano Nascimento: " ,+ ano_nascimento)
print("Idade: " ,+ Idade)
