import tkinter as tk
from nova_tela import abrir_jogo_parimpar

# Janela principal
janela = tk.Tk()
janela.title("Tela Principal")
janela.geometry("300x200")

# Botão que chama a nova tela
botao = tk.Button(janela, text="Abrir nova tela", command=lambda: abrir_jogo_parimpar(janela))
botao.pack(pady=50)

janela.mainloop()