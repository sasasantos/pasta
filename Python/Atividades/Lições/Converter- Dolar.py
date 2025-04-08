import os

os.system("cls")

print("Conversor de Dólar para Real")

cotação = float(input("Digite a cotação do Dólar: "))

dolar = float(input("Digite o valor em Dólar: "))

real = (cotação * dolar)

os.system("cls")

print("Cotação do Dólar: " ,+ cotação)
print("Valor em Dólar: " ,+ dolar)
print("Valor em Real: " ,+ real)
