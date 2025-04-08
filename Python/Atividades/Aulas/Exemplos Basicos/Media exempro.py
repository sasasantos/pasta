import os

#Limpando a tela
os.system("cls")

#1 passo - Entrada de dados
print("Projeto Boletim")

nome = input("Entre com o nome do aluno: ")

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

#2 passo - Conta
Media = (nota01 + nota02 + nota03) / 3

#3 passo - Saída
os.system("cls")

print("Nome do usuário: " + nome)
print("Valor do primeiro nota: " , nota01)
print("Valor do segundo nota: " , nota02)
print("Valor do terceiro nota: " , nota03)
print("Valor final: " , Media)

if(Media >= 7):
    print("Você foi Aprovado!")

elif(Media >= 5 and Media <7):
    print("Você ficou de recuperação!")

else:
    print("Você foi Reprovado!")

