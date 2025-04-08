import os

os.system("cls")

print("Conversor de Temperatura")

celsius = float(input("Digite a temperatura: "))

fahrenheit= (9 * celsius + 160) / 5

os.system("cls")

print("Temperatura Celsius: " ,+ celsius)
print("Temperatura em Fahrenheit: " ,+ fahrenheit)
