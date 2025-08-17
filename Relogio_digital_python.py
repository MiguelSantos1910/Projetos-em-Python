import tkinter as tk
import winsound
from datetime import datetime
from tkinter import messagebox

contador = 0 
hora_alarme = None
opcao = None
botao_parar = None
label_cancelar_alarme = None

def atualizar_relogio():
    global hora_alarme
    agora = datetime.now()
    hora = agora.strftime("%H:%M:%S")
    data = agora.strftime("%d/%m/%Y")
    
    label_hora.config(text=hora)
    label_data.config(text=data)
    
    if hora_alarme == hora:
        winsound.Beep(1000, 1000)
        piscar_alarme()
        messagebox.showinfo("Alarme", f"É {hora_alarme}! Alarme disparado.")
        hora_alarme = None
        if opcao:
            opcao.config(state="disabled")
        if botao_parar:
            botao_parar.pack()
    
    janela.after(1000, atualizar_relogio)

def estilo():
    global contador
    if contador == 0:
        label_hora.config(font=("Times New Roman", 40), fg="blue", bg="black")
        label_data.config(font=("Times New Roman", 20), fg="white", bg="black")
    elif contador == 1:
        label_hora.config(font=("Arial", 40), fg="white", bg="black")
        label_data.config(font=("Arial", 20), fg="green", bg="black")
    elif contador == 2:
        label_hora.config(font=("Courier New", 40), fg="yellow", bg="black")
        label_data.config(font=("Courier New", 20), fg="black", bg="white")
    elif contador == 3:
        label_hora.config(font=("Comic Sans MS", 40), fg="green", bg="black")
        label_data.config(font=("Comic Sans MS", 20), fg="white", bg="black")
    elif contador == 4:
        label_hora.config(font=("Verdana", 40, "bold"), fg="cyan", bg="darkgreen")
        label_data.config(font=("Verdana", 20), fg="white", bg="darkgreen")
        
    contador = (contador + 1) % 5

def definir_alarme_relogio():
        global hora_alarme
        valor = opcao.get()
        try:
            datetime.strptime(valor, "%H:%M:%S")
            hora_alarme = valor
        except ValueError:
            messagebox.showerror("Erro", "Formato Invalido. Use HH:MM:SS")
  
def alarme_relogio():
    global opcao
    opcao = tk.Entry(janela, width=15)
    opcao.pack(pady=5)
    botao_definir = tk.Button(janela, text="Confirmar Alarme", command=definir_alarme_relogio)
    botao_definir.pack(pady=5)

def atualizar_cor_relogio():
    botao_lateral = tk.Frame(janela, bg="black", width=100)
    botao_lateral.pack(side="top", fill="x")
    botao = tk.Button(botao_lateral, text="Alterar Estilo", command=estilo)
    botao.pack(pady=20)
    
def piscar_alarme(cor=0):
    cores = [("green", "black"), ("yellow", "black")]
    fg, bg = cores[cor % len(cores)]
    label_hora.config(fg=fg, bg=bg)
    if cor < 6:  # piscar 3 vezes
        janela.after(300, lambda: piscar_alarme(cor + 1))

def alarme():
    global opcao
    botao_lateral_alarme = tk.Frame(janela, bg="black")
    botao_lateral_alarme.pack(side="top", fill="x")
    botao_alarme = tk.Button(botao_lateral_alarme, text="Definir alarme", command=alarme_relogio)
    botao_alarme.pack(pady=5)
    label_instrucao = tk.Label(janela, text="Formato: (HH:MM:SS)", bg="black", fg="white")
    label_instrucao.pack()

def cancelar_alarme():
    global hora_alarme
    hora_alarme = None
    label_cancelar_alarme.config(text="Alarme Cancelado!", fg="red")
    if botao_parar:
        botao_parar.pack_forget()
    
def botao_cancelar_alarme():
     global botao_parar
     botao_lateral_cancelar_alarme = tk.Frame(janela, bg="black")
     botao_lateral_cancelar_alarme.pack(side="top", fill="x")
     botao_parar = tk.Button(botao_lateral_cancelar_alarme, text="Cancelar Alarme", command=cancelar_alarme)
     botao_parar.pack(pady=5)
     botao_parar.pack_forget()

# def botao_janela2():
#     if botao_janela2():
        

# Janela principal
janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("300x200")
janela.configure(bg="#1e1e1e")

# Janela secundaria
janela2 = tk.Tk()
janela.title("Informaçoes do Projeto")
janela.geometry("300x200")
janela.configure(bg="#1e1e1e")


# Layout janela
relogio_layout = tk.Frame(janela, bg="black", width=100)
relogio_layout.pack(side="right", expand=True, fill="both")

# Labels default
label_hora = tk.Label(relogio_layout, font=("Helvetica", 40), fg="green", bg="black")
label_hora.pack(pady=10)
label_data = tk.Label(relogio_layout, font=("Helvetica", 20), fg="white", bg="black")
label_data.pack()
label_cancelar_alarme = tk.Label(janela, text="", bg="black", fg="white")
label_cancelar_alarme.pack(pady=5)

atualizar_cor_relogio()
alarme()
botao_cancelar_alarme()
atualizar_relogio()

janela.mainloop()