numero = 0
soma = float
contador = 0
while True:
    try:
        opcao = str(input("Selecione a operação desejada:"))
        opcao2 = float(input("Digíte um número:"))
        opcao3 = float(input("Digíte um número:"))
        if opcao == 'adição':
            soma = opcao2 + opcao3
            print(">" * 70)
            print(f"O número {opcao2} somado com o número {opcao3}, resulta em: {soma:.2f}")
        elif opcao == 'subtração':
            soma = opcao2 - opcao3
            print(f"O número {opcao2} subtraído com o número {opcao3}, resulta em: {soma:.2f}")
            print(">" * 70)
        elif opcao == 'multiplicação':
            soma = opcao2 * opcao3
            print(">" * 70)
            print(f"O número {opcao2} multiplicado com o número {opcao3}, resulta em: {soma:.2f}")
        elif opcao == 'divisão':
            soma = opcao2 / opcao3
            print(">" * 70)
            print(f"O número {opcao2} dividido com o número {opcao3}, resulta em: {soma:.2f}")
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
    except ZeroDivisionError:
        print("Não é possível dividir números por zero! Tente novamente.")