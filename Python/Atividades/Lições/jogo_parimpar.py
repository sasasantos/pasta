import os

os.system("cls")

from tkinter import *

def verificar ():
    try:
        numero = int (entry_numero.get())
        if numero % 2 == 0:
            resultado_label.config(text = f"{numero} é Par!")
        else:
            resultado_label.config(text = f"{numero} é Ímpar!")
    except ValueError:
        resultado_label.config(text = "Por favor, insira um número válido.")
    
cor1= 'dark blue'

janela = Tk()
janela.title("Sistema Par ou Ímpar")
janela.geometry("400x300")
janela.config(bg = cor1)

titulo_label = Label (janela, text= "Escolha um número Par ou Ímpar", font=("Arial", 14), bg = "dark blue", fg = "white")
titulo_label.pack(pady=10)

entrada_label = Label (janela, text= "Digite um número: ", font=("Arial", 14), bg = "dark blue", fg = "white")
entrada_label.pack()

entry_numero = Entry (janela, font=("Arial", 14), bg = "white", fg = "black")   
entry_numero.pack(pady=5)

verificar_btn= Button (janela, text= "Verificar", font=("Arial", 14), bg = "white", fg = "black", command= verificar)
verificar_btn.pack(pady=10)

resultado_label = Label (janela, text= "", font=("Arial", 14, "bold"), bg = "dark blue", fg = "white")
resultado_label.pack(pady=10)

janela.mainloop()