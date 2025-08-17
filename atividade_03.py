import time
import os
import tkinter.messagebox
from os import remove
from tkinter.messagebox import YESNO
from docutils.nodes import option
from pyexpat.errors import messages
chegada = 0
ativo = []
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("Para sair do programa digíte 'exit' no lugar do nome.")
    try:
        nome = str(input("Digíte seu nome:"))
        if nome == "exit":
            resposta = tkinter.messagebox.askyesno(title="Fim de Programa", message="Deseja sair do programa?", type=YESNO)
            if resposta:
                break
            else:
                continue
        idade = int(input("Digíte sua idade:"))
        categoria_chamada = ["Gestante ou criança de colo", "Idoso", "PCD", "Demais público"]
        categoria = input(f"Selecione sua categoria: [1] -> {categoria_chamada[0]}, [2] -> {categoria_chamada[1]}, [3] -> {categoria_chamada[2]}, [4] -> {categoria_chamada[3]}:")
        chegada += 1
        if categoria == "1":
            categoria = categoria_chamada[0]
        if categoria == "2" or idade >= 65:
            categoria = categoria_chamada[1]
        if categoria == "3":
            categoria = categoria_chamada[2]
        if categoria == "4":
            categoria = categoria_chamada[3]
        cadastro = nome, idade, categoria
        prioridade = [categoria_chamada[1], categoria_chamada[0], categoria_chamada[3], categoria_chamada[2]]
        clear()
        print(f"Você selecionou: {categoria}")
        time.sleep(1)
        print(f"Dados cadastrados = Nome: {nome}, Idade: {idade}, Categoria: {categoria}, Nº chegada: {chegada}")
        time.sleep(1)
        clear()
        while chegada >= 2:
            for categoria in prioridade:
                ativo.append(prioridade)
                if categoria not in prioridade:
                    ativo.append(cadastro)
            print(f"Em preparação: {ativo}")
            break
    except ValueError:
        print("Você digítou algum caractere inválido!")
        print("Tente novamente!")