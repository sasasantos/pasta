import os

os.system("cls")

cotacao = float(input("Digite a cotação do dollar: "))

print("----------------------------------------------------------------------")
print("-----------------------ESCOLHA UMA OPÇÃO------------------------------")
print("----------------------------------------------------------------------")

opcao = int(input("1- Converter dollar para real ou 2- Converter de real para dollar: "))

if opcao == 1:
    valor = float(input("Digite o valor em dollar a ser convertido para real: "))
    resultado = valor * cotacao
    print(f"O valor em reais é:  {resultado}")

elif opcao == 2:
    valor1 = float(input("Digite o valor em reais a ser convertido para dollar: "))
    resultado1 = valor1 / cotacao
    print(f"O valor em dollar é: {resultado1}")

else:
    print("Digite uma opção válida")

input("Pressione <Enter> para continuar ...")