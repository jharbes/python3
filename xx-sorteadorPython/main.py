import tkinter as tk
import random

def sortear():
    numero_sorteado = random.randint(1, 100)
    label_resultado.config(text=f"O número sorteado é: {numero_sorteado}")

# Cria a janela principal
janela = tk.Tk()
janela.title("Sorteador de Números")
janela.geometry("300x200")

# Cria os widgets
label_titulo = tk.Label(janela, text="Sorteador de Números", font=("Arial", 16))
label_titulo.pack(pady=10)

botao_sortear = tk.Button(janela, text="Sortear", command=sortear)
botao_sortear.pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Inicia o loop da janela
janela.mainloop()
