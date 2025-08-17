import os
import tkinter.messagebox
from operator import itemgetter

# Limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dicionário com a prioridade de cada tipo de pedido
prioridade_entrega = {
    "Drive-Thru": 1,
    "Local": 2,
    "Ifood": 3
}

# Lista para armazenar todos os pedidos
pedidos = []

while True:
    print("Digite 'sair' no nome para encerrar.")
    nome = input("Digite seu nome: ")

    if nome.lower() == "sair":
        resposta = tkinter.messagebox.askyesno(title="Fim do Programa", message="Deseja sair do programa?")
        if resposta:
            break
        else:
            continue

    pedido = input("Digite seu pedido: ")

    print("\nSelecione o tipo de entrega:")
    print("[1] Drive-Thru")
    print("[2] Local")
    print("[3] Ifood")
    tipo_input = input("Opção: ")

    if tipo_input == "1":
        tipo = "Drive-Thru"
    elif tipo_input == "2":
        tipo = "Local"
    elif tipo_input == "3":
        tipo = "Ifood"
    else:
        print("Opção inválida. Pedido cancelado.\n")
        continue

    cadastro = {
        "nome": nome,
        "pedido": pedido,
        "tipo": tipo,
        "prioridade": prioridade_entrega[tipo]
    }

    pedidos.append(cadastro)
    clear()
    print(f"Pedido registrado com sucesso! Nome: {nome}, Pedido: {pedido}, Tipo: {tipo}\n")

    if len(pedidos) >= 2:
        pedidos_ordenados = sorted(pedidos, key=itemgetter("prioridade"))
        print("Fila de atendimento por ordem de entrega:")
        for p in pedidos_ordenados:
            print(f"- {p['nome']} pediu '{p['pedido']}' via {p['tipo']}")
        print()
