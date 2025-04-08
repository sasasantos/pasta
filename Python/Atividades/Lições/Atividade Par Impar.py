import os

os.system("cls")

print("Números Pares ou Ímpares")

numero = int(input("Digite o número: "))

conta = numero % 2

if(conta == 0):
    print("Seu número é PAR")

elif(conta == 1):
    print("Seu número é IMPAR")