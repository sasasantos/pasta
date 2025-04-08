import os

#limpando a tela
os.system("cls")

#1 passo - realizar entrada de dados
print("Projeto Soma \n")
print("================================ \n")

nome = input("Digite o seu nome: ")
valor01 = int(input("Digite um valor: "))
valor02 = int(input("Digite um valor: "))

#2 passo - Realizar o processamento
Soma = valor01 + valor02

#3 passo - Saída
os.system("cls")

print("Nome do usuário: " + nome)
print("Valor do primeiro número: " , valor01)
print("Valor do segundo número: " , valor02)
print("Valor final: " , Soma)
