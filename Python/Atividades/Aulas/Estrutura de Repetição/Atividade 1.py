import os

os.system("cls")

print("Tabuada")

numero = int(input("Digite um número: "))

os.system("cls")

contador = 0
while contador < 11:
    conta = contador * numero
    print(contador , "x"  , numero , "=" , conta)
    contador += 1