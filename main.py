import funcoes as f
import os

def menu():
    lista = []
    while True:
        print("=====CALCULADORA DE CONSUMO ENERGÉTICO=====\n"
              "1. Adicionar aparelho\n"
              "2. Listar aparelhos\n"
              "3. Calcular consumo diário\n"
              "4. Calcular consumo mensal\n"
              "5. Gerar gráfico de barras\n"
              "6. Gerar gráfico de pizza\n"
              "0. Sair")
        try:
            opcao = int(input("Escola a opção: "))
            os.system('cls')
            if opcao == 1:
                nome = input("Nome do aparelho: ")
                potencia = float(input("Potência (W): "))
                horas = float(input("Horas por dia: "))
                quantidade = int(input("Quantidade: "))
                f.adicionaAparelho(lista, nome, potencia, horas, quantidade)
                print("Aparelho adicionado com sucesso!\n"
                      "")
            elif opcao == 2:
                f.listarAparelhos(lista)
            elif opcao == 3:
                f.calcularConsumoDiario(lista)
            elif opcao == 4:
                f.calcularConsumoMensal(lista)
            elif opcao == 5:
                f.gerarGraficoBarrasDiarioeMensal(lista)
            elif opcao == 6:
                f.gerarGraficoPizzaDiarioeMensal(lista)
            elif opcao == 0:
                print("Saindo da calculadora.")
                break
            else:
                print("Opção inválida. Escolha uma opção entre 0 e 6.")
        except ValueError:
            print("Entrada inválida. Por favor digite números válidos.\n")