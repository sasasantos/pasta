import os

os.system("cls")

import tkinter as tk

def abrir_nova_tela():
    media_sintese = tk.Toplevel()
    media_sintese.title("Nova Tela")
    media_sintese.geometry("300x200")
    tk.Label(media_sintese, text="Essa é a nova tela!").pack(pady=20)
    tk.Button(media_sintese, text="Fechar", command=media_sintese.destroy).pack()

# Janela principal
janela = tk.Tk()
janela.title("Tela Principal")
janela.geometry("300x200")

botao = tk.Button(janela, text="Abrir nova tela", command=abrir_nova_tela)
botao.pack(pady=50)