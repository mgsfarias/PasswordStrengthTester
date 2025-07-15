import tkinter as tk
import re

def verificar_forca():
    senha = entrada.get()
    forca = 0
    dicas = []

    if len(senha) >= 8: forca += 1
    else: dicas.append("Use ao menos 8 caracteres.")
    if re.search("[a-z]", senha) and re.search("[A-Z]", senha): forca += 1
    else: dicas.append("Use letras maiúsculas e minúsculas.")
    if re.search("\d", senha): forca += 1
    else: dicas.append("Inclua números.")
    if re.search("[^A-Za-z0-9]", senha): forca += 1
    else: dicas.append("Inclua símbolos.")

    niveis = ["Muito Fraca", "Fraca", "Média", "Boa", "Forte"]
    resultado["text"] = f"Força: {niveis[forca]}"
    sugestoes["text"] = "\n".join(dicas)

janela = tk.Tk()
janela.title("Verificador de Senhas")

tk.Label(janela, text="Digite sua senha:").pack()
entrada = tk.Entry(janela, show="*")
entrada.pack()

tk.Button(janela, text="Verificar", command=verificar_forca).pack()
resultado = tk.Label(janela, text="Força: -")
resultado.pack()

sugestoes = tk.Label(janela, text="", fg="red")
sugestoes.pack()

janela.mainloop()
