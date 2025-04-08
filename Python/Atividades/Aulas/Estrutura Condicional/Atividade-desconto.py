import os

os.system("cls")

print("Projeto Desconto")

nome = input("Digite o nome do produto: ")

valor = float(input("Digite o preço do produto: "))

item = int(input("Digite a quantidade de produtos comprados: "))

conta = valor * item
print("Valor da compra final sem desconto:", + conta)

if(item <= 5):
    desconto1 = conta- (0.02 * conta)
    print("Valor final com desconto 2% de desconto", + desconto1)

elif(item > 5 and item <= 10):
    desconto2 = conta- (0.03 * conta)
    print("Valor final com desconto 3% de desconto", + desconto2)

else:
    (item > 10)
    desconto3 = conta- (0.05 * conta)
    print("Valor final com desconto 5% de desconto", + desconto3)
