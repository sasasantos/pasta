import os

os.system("cls")

print("Projeto IMC")

nome = input("Digite o seu nome: ")

peso = float(input("Digite o seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura) 
print("Seu IMC é: " ,  imc)

if(imc < 16.9):
    print("Você está muito abaixo do peso!")

elif(imc >= 17 and imc <= 18.4):
    print("Você está abixou do peso!")

elif(imc >= 18.5 and imc <= 24.9):
    print("Você está no peso normal!")

elif(imc >= 25 and imc <= 29.9):
    print("Você está acima do peso!")

elif(imc >= 30 and imc <= 34.9):
    print("Você está com Obesidade nivel 1!")

elif(imc >= 35 and imc <= 40):
    print("Você está com Obesidade nivel 2!")

else:
    print("Você está com Obesidade nivel 3!")