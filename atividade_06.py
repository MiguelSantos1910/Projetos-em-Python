import time
opcao1 = int(input("Digíte algum valor:"))
opcao2 = int(input("Digíte algum valor:"))
if opcao1 > opcao2:
    print("O modelo selecionado, de acordo com os números digítados foi de ORDEM DECRESCENTE")
    time.sleep(2)
    print(">" * 70)
    for numero in range(10, 0, -1):
        time.sleep(0.5)
        print(numero)
if opcao2 > opcao1:
    print("O modelo selecionado, de acordo com os números digítados foi de ORDEM CRESCENTE")
    time.sleep(2)
    print(">" * 70)
    for numero2 in range(0, 11, 1):
        time.sleep(0.5)
        print(numero2)