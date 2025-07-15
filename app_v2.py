# Projeto: Verificador de Força de Senhas com Interface Moderna (Tkinter + ttkbootstrap)

import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
import re
import math

# Cálculo aproximado do tempo de quebra de senha via brute force
def estimar_tempo_bruteforce(senha):
    charset = 0
    if re.search(r"[a-z]", senha): charset += 26
    if re.search(r"[A-Z]", senha): charset += 26
    if re.search(r"\d", senha): charset += 10
    if re.search(r"[^A-Za-z0-9]", senha): charset += 32

    combinacoes = charset ** len(senha)
    tentativas_por_segundo = 1_000_000_000  # 1 bilhão/s
    segundos = combinacoes / tentativas_por_segundo

    if segundos < 1:
        return "0 segundos"
    unidades = ["segundos", "minutos", "horas", "dias", "anos", "séculos"]
    fatores = [60, 60, 24, 365, 100]

    for i in range(len(fatores)):
        if segundos < fatores[i]:
            return f"{int(segundos)} {unidades[i]}"
        segundos /= fatores[i]

    return f"{int(segundos)} {unidades[-1]}"

# Função principal de análise de senha
def analisar_senha(event=None):
    senha = entrada.get()
    requisitos = {
        'Letras minúsculas': bool(re.search(r"[a-z]", senha)),
        'Letra maiúscula': bool(re.search(r"[A-Z]", senha)),
        'Números': bool(re.search(r"\d", senha)),
        'Símbolos': bool(re.search(r"[^A-Za-z0-9]", senha)),
        '8 caracteres': len(senha) >= 8
    }

    for label, status in requisitos.items():
        cores[label].configure(foreground="green" if status else "gray")

    pontuacao = sum(requisitos.values())
    classificacoes = [
    ("Muito fraco", "danger"),
    ("Fraco", "danger"),
    ("Médio", "warning"),
    ("Bom", "warning"),
    ("Forte", "success")
]

    indice = pontuacao - 1 if pontuacao > 0 else 0
    texto, estilo = classificacoes[indice]

    barra.configure(value=pontuacao)
    barra.configure(text=texto)      # <-- Aqui é onde o nome muda
    barra.configure(bootstyle=estilo)

    texto_resultado.set(classificacoes[pontuacao - 1] if pontuacao > 0 else "Muito fraco")

    tempo = estimar_tempo_bruteforce(senha)
    texto_tempo.set(f"Tempo necessário para decifrar essa senha: {tempo}")

# Cria janela com tema moderno
# tema = tb.ThemedTk(theme="flatly") <- descontinuada
tema = tb.Window(themename="flatly")
tema.title("Verificador de Senha Segura")
tema.geometry("450x350")
tema.resizable(False, False)

texto_resultado = tk.StringVar()
texto_tempo = tk.StringVar()

# Entrada de senha
tb.Label(tema, text="Digite sua senha:").pack(pady=(20, 5))
entrada = tb.Entry(tema, width=35, font=("Arial", 12))
entrada.pack()
entrada.bind("<KeyRelease>", analisar_senha)

# Barra de força
barra = tb.Floodgauge(
    tema,
    value=0,
    maximum=5,
    bootstyle="danger",
    font=("Arial", 12),
    text="Muito fraco"
)
barra.pack(pady=10)

# Critérios
frame_criterios = ttk.Frame(tema)
frame_criterios.pack()

criterios = ['8 caracteres', 'Letras minúsculas', 'Letra maiúscula', 'Números', 'Símbolos']
cores = {}

for i, crit in enumerate(criterios):
    lbl = ttk.Label(frame_criterios, text=crit, foreground="gray")
    lbl.grid(row=0, column=i, padx=4)
    cores[crit] = lbl

# Resultado
tb.Label(tema, textvariable=texto_tempo, font=("Arial", 10), foreground="red").pack(pady=10)

# Inicia a aplicação
tema.mainloop()
