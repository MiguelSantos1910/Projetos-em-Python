opcao1 = 0
opcao2 = 0
opcao3 = 0
opcao4 = 0
opcao5 = str
escolha1 = "crescente"
escolha2 = "decrescente"
while True:
    opcao5 = str(input("Selecione se a ordem dos números será crescente ou decrescente:"))
    print(f"Você selecionou na ordem {opcao5}.")
    if opcao5 == escolha1:
        contador = 0
        while contador < 4:
                if contador == 0:
                    opcao1 = int(input("Digíte um número qualquer:"))
                elif contador == 1:
                    opcao2 = int(input("Digíte um número qualquer:"))
                elif contador == 2:
                    opcao3 = int(input("Digíte um número qualquer:"))
                elif contador == 3:
                    opcao4 = int(input("Digíte um número qualquer:"))
                contador = contador + 1
        if opcao1 > opcao2:
            opcao1, opcao2 = opcao2, opcao1
        if opcao2 > opcao3:
            opcao2, opcao3 = opcao3, opcao2
        if opcao3 > opcao4:
            opcao3, opcao4 = opcao4, opcao3
        if opcao1 > opcao2:
            opcao1, opcao2 = opcao2, opcao1
        if opcao2 > opcao3:
            opcao2, opcao3 = opcao3, opcao2
        if opcao1 > opcao2:
            opcao1, opcao2 = opcao2, opcao1
        print(f"{opcao1}, {opcao2}, {opcao3}, {opcao4}")
    if opcao5 == escolha2:
        contador = 0
        while contador < 4:
                if contador == 0:
                    opcao1 = int(input("Digíte um número qualquer:"))
                elif contador == 1:
                    opcao2 = int(input("Digíte um número qualquer:"))
                elif contador == 2:
                    opcao3 = int(input("Digíte um número qualquer:"))
                elif contador == 3:
                    opcao4 = int(input("Digíte um número qualquer:"))
                contador = contador + 1
        if opcao1 < opcao2:
            opcao1, opcao2 = opcao2, opcao1
        if opcao2 < opcao3:
            opcao2, opcao3 = opcao3, opcao2
        if opcao3 < opcao4:
            opcao3, opcao4 = opcao4, opcao3
        if opcao1 < opcao2:
            opcao1, opcao2 = opcao2, opcao1
        if opcao2 < opcao3:
            opcao2, opcao3 = opcao3, opcao2
        if opcao1 < opcao2:
            opcao1, opcao2 = opcao2, opcao1
        print(f"{opcao1}, {opcao2}, {opcao3}, {opcao4}")