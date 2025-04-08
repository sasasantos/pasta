import os

try:
    os.system("cls")

    print("Projeto Professor")

    nome = input("Digite o nome do professor: ")
    nivel = int(input("Digite seu nível: "))
    aulas = int(input("Digite quantas aulas foram realizadas por semana: "))

    if(nivel == 1):
        nivel1 = (aulas * 12)
        print("Seu salario mensal é: " , + nivel1)

    elif(nivel == 2):
        nivel2 = (aulas * 17)
        print("Seu salario mensal é: ", + nivel2)

    else:
        (nivel == 3)
        nivel3 = (aulas * 25)
        print("Seu salario mensal é: ", + nivel3)
        
except Exception as erro:
    print(f"Aconteceu um erro: {erro} ")