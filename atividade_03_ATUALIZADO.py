import time
import os
import tkinter.messagebox
from tkinter.messagebox import YESNO
from operator import itemgetter

chegada = 0
fila = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define ordem de prioridade (menor número = maior prioridade)
prioridade_valores = {
    "Idoso": 1,
    "Gestante ou criança de colo": 2,
    "PCD": 3,
    "Demais público": 4
}

categoria_chamada = ["Gestante ou criança de colo", "Idoso", "PCD", "Demais público"]

while True:
    print("Para sair do programa digite 'exit' no lugar do nome.")
    try:
        nome = str(input("Digite seu nome: "))
        if nome == "exit":
            resposta = tkinter.messagebox.askyesno(title="Fim de Programa", message="Deseja sair do programa?", type=YESNO)
            if resposta:
                break
            else:
                continue

        idade = int(input("Digite sua idade: "))
        categoria_input = input(f"Selecione sua categoria: [1] -> {categoria_chamada[0]}, [2] -> {categoria_chamada[1]}, [3] -> {categoria_chamada[2]}, [4] -> {categoria_chamada[3]}: ")

        chegada += 1

        if categoria_input == "1":
            categoria = categoria_chamada[0]
        elif categoria_input == "2" or idade >= 65:
            categoria = categoria_chamada[1]
        elif categoria_input == "3":
            categoria = categoria_chamada[2]
        elif categoria_input == "4":
            categoria = categoria_chamada[3]
        else:
            print("Opção inválida, cadastro cancelado.")
            continue

        cadastro = {
            "nome": nome,
            "idade": idade,
            "categoria": categoria,
            "chegada": chegada,
            "prioridade": prioridade_valores[categoria]
        }

        fila.append(cadastro)

        clear()
        print(f"Você selecionou: {categoria}")
        time.sleep(1)
        print(f"Dados cadastrados = Nome: {nome}, Idade: {idade}, Categoria: {categoria}, Nº chegada: {chegada}")
        time.sleep(1)
        clear()

        if len(fila) >= 2:
            fila_ordenada = sorted(fila, key=itemgetter("prioridade", "chegada"))
            print("Fila de atendimento (por prioridade):")
            for pessoa in fila_ordenada:
                print(f"- Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Categoria: {pessoa['categoria']}, Chegada: {pessoa['chegada']}")
            print()

    except ValueError:
        print("Você digitou algum caractere inválido!")
        print("Tente novamente!")

