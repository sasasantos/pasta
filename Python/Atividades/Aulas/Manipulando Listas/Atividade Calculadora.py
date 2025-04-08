import os

try:
    os.system("cls")

    print("Projeto Calculadora")

    numero1 = int(input("Digite o primeiro número: "))

    numero2 = int(input("Digite o segundo número: "))

    caracter = int(input("Digite 1 para soma, 2 para multiplicação, 3 para divisão e 4 para subtração: "))

    if(caracter == 1):
        print("Soma")
        conta1 = numero1 + numero2
        print("Seu resultado é:", + conta1)

    elif(caracter == 2):
        print("Multiplicação")
        conta2 = numero1 * numero2
        print("Seu resultado é:", + conta2)

    elif(caracter == 3):
        print("Divisão")
        conta3 = numero1 / numero2
        print("Seu resultado é:", + conta3)

    else:
        print("Subtração")
        conta4 = numero1 - numero2
        print("Seu resultado é:", + conta4)
    
except Exception as erro:
    print(f"Aconteceu um erro: {erro} ")