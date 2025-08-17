dados_1 = []
dados_2 = []
menor = []
maior = []
contador = 0
while True:
    try:
        opcao = int(input("Digíte um número qualquer:"))
        opcao2 = int(input("Digite outro número:"))
        dados_1.append(opcao)
        dados_2.append(opcao2)
    except ValueError:
        print("Você digitou um caractere não numérico")
    if contador == 4:
        for i in range(len(dados_1)):
            for i in range(len(dados_2)):
                maximo = max(dados_1[i], dados_2[i])
                maior.append(maximo)
                mn = min(dados_1[i], dados_2[i])
                menor.append(mn)
            print("O valor máximo é de:", maior)
            print("O valor mínimo é de:", mn)
            break
        break
    contador += 1