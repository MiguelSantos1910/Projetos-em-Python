contador = 0
while True:
    try:
        opcao = int(input("Digíte o seu sálario:"))
        opcao2 = int(input("Digíte o valor da casa:"))
        opcao3 = int(input("Digíte a quantidade de anos a pagar:"))
        valor_prestacao = opcao2 / (opcao3 * 12)
        if valor_prestacao > opcao * 0.3:
            print("O empréstimo não pode ser efetuado, pois seu salário e inferior a prestação!")
        else:
            print("O empréstimo foi efetuado com sucesso!")
            print(f"O valor mensal da prestação será de: R${valor_prestacao:.2f}")
    except ValueError:
        print("Você digitou um caractere não numérico")
        print("Tente novamente!")
        contador += 1
        if contador == 1:
            print(f"Você tem apenas tentativas de digitação, digíte apenas caracteres numéricos!")
            print(f"Tentativa {contador}")
        if contador == 2:
            print(f"Você tem apenas 3 tentativas de digitação, digíte apenas caracteres numéricos!")
            print(f"Tentativa {contador}")
        if contador == 3:
            print(f"Você tem apenas 3 tentativas de digitação, digíte apenas caracteres numéricos!")
            print(f"Tentativa {contador}")
            break