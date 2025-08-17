import matplotlib.pyplot as plt
from main import menu

def adicionaAparelho(lista, nome, potencia, horas, quantidade):
    aparelhos = {
        'nome': nome,
        'potencia': potencia,
        'horas': horas,
        'quantidade': quantidade
    }
    lista.append(aparelhos)
    return aparelhos

def listarAparelhos(lista):
    for i, aparelho in enumerate(lista, 1):
        print(f"Aparelho {i}:")
        print(f"  Nome: {aparelho['nome']}")
        print(f"  Potência (W): {aparelho['potencia']}")
        print(f"  Horas de uso por dia: {aparelho['horas']}")
        print(f"  Quantidade: {aparelho['quantidade']}")
        print("-" * 20)


def calcularConsumoDiario(lista):
    print("Consumo diário por aparelho:")
    consumo_total = 0
    for aparelho in lista:
        consumo = (aparelho['potencia'] * aparelho['horas'] * aparelho['quantidade']) / 1000
        consumo_total += consumo
        print(f"-{aparelho['quantidade']}X {aparelho['nome']} consome {consumo:.2f} kWh/dia")
    print(f"Consumo diário total: {consumo_total:.2f} kWh\n")

def calcularConsumoMensal(lista):
    print("Consumo mensal por aparelho:")
    consumo_total = 0
    for aparelho in lista:
        consumo = (aparelho['potencia'] * aparelho['horas'] * aparelho['quantidade'] * 30) / 1000
        consumo_total += consumo
        print(f"-{aparelho['quantidade']}X {aparelho['nome']} consome {consumo:.2f} kWh/mês")
    print(f"Consumo mensal total: {consumo_total:.2f} kWh\n")

def gerarGraficoBarrasDiarioeMensal(lista):
    nomes = [aparelho['nome'] for aparelho in lista]
    consumo_diario = [((aparelho['potencia'] * aparelho['horas'] * aparelho['quantidade'])) / 1000 for aparelho in lista]
    consumo_mensal = [((aparelho['potencia'] * aparelho['horas'] * aparelho['quantidade'] * 30)) / 1000 for aparelho in lista]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].bar(nomes, consumo_diario, color='blue')
    axes[0].set_title("Consumo diário por aparelho")
    axes[0].set_xlabel("Aparelhos")
    axes[0].set_ylabel("Consumo (kWh)")
    axes[0].tick_params(axis='x', rotation=45)

    axes[1].bar(nomes, consumo_mensal, color='green')
    axes[1].set_title("Consumo mensal por aparelho")
    axes[1].set_xlabel("Aparelhos")
    axes[1].set_ylabel("Consumo (kWh)")
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

def gerarGraficoPizzaDiarioeMensal(lista):
    nomes = [aparelho['nome'] for aparelho in lista]
    consumo_diario = [((aparelho['potencia'] * aparelho['horas'] * aparelho['quantidade'])) / 1000 for aparelho in lista]
    consumo_mensal = [((aparelho['potencia'] * aparelho['horas'] * aparelho['quantidade'] * 30)) / 1000 for aparelho in lista]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].pie(consumo_diario, labels=nomes, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    axes[0].set_title("Distribuição do consumo diário")

    axes[1].pie(consumo_mensal, labels=nomes, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    axes[1].set_title("Distribuição do consumo mensal")

    plt.tight_layout()
    plt.show()



lista = []

menu()