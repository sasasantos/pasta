import os

def limpar_tela():
    os.system("cls")

def obter_cotacao():
    return float(input("Qual a cotação do Dólar? "))

def converter_dolar_para_real(cotacao):
    valor = float (input("Qual o valor em Dólar a ser convertido para Real? "))
    return valor * cotacao

def converter_real_para_dolar(cotacao):
    valor = float(input("Qual o valor em Real a ser convertido para Dólar? "))
    return valor / cotacao

