import os
import time
import tkinter
entrega_pedido = 0
pedidos = []
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
entrega = ["Ifood", "Local", "Drive-Thru"]
while True:
    print("Para sair do programa digíte 'exit' no lugar do nome.")
    nome = str(input("Digíte seu nome:"))
    if nome == "exit":
        resposta = tkinter.messagebox.askyesno(title="Fim de Programa", message="Deseja sair do programa?", type=YESNO)
        if resposta:
            break
        else:
            continue
    pedido = int(input("Combo 1 -> 0, Combo 2 -> 1, Combo 3 -> 2 \n"
                       "Digíte o número do pedido:"))
    tipo = int(input("1 -> Ifood, 2 -> Local, 3 -> Drive-Trhu \n"
                     "Selecione o tipo de entrega:"))
    if pedido == 0:
        print("Você selecionou o Combo 1")
    if pedido == 1:
        print("Você selecionou o Combo 2")
    if pedido == 2:
        print("Você selecionou o Combo 3")
    if tipo == 1:
        tipo = entrega[0]
    if tipo == 2:
        tipo = entrega[1]
    if tipo == 3:
        tipo = entrega[2]
    cadastro = nome, pedido, tipo
    prioridade_pedidos = [entrega[2], entrega[1], entrega[0]]
    entrega_pedido += 1
    clear()
    print(f"Você selecionou o modelo de entrega: {tipo}")
    time.sleep(1)
    print(f"Dados cadastrados = Nome: {nome}, pedido: {pedido}, Formato: {tipo}, Nº pedido: {entrega_pedido}")
    time.sleep(1)
    clear()
    while entrega_pedido >= 2:
        for tipo in prioridade_pedidos:
            pedidos.append(tipo)
            if tipo not in prioridade_pedidos:
                pedidos.append(cadastro)
        print(f"Em andamento: {pedido}")
        print(f"Em preparação: {cadastro}")
        break