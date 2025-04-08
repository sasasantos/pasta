import os

os.system("cls")

print("Atividade Idade do Jogador")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if(idade <=13):
    print("Sua categoria é INFANTIL")

elif(idade >13 and idade <=17):
    print("Sua categoria é JUVENIL")

else:
    print("Sua categoria é SÊNIOR ")