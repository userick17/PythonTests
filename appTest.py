# -*- coding: utf-8 -*-

import Tkinter as tk
import tkSimpleDialog

# Crie uma janela
app = tk.Tk()
app.title("Aplicação de Exemplo")

# Adicione widgets
label = tk.Label(app, text="Hello to world of penguins!")
label.pack(padx=20, pady=20)

# Função de exemplo para um diálogo simples
def show_dialog():
    user_input = tkSimpleDialog.askstring("Input", "Digite algo:")
    if user_input:
        print("Você digitou: " + user_input)

# Botão para mostrar o diálogo
button = tk.Button(app, text="Abrir Diálogo", command=show_dialog)
button.pack(padx=10, pady=10)

# Inicie o loop principal
app.mainloop()
