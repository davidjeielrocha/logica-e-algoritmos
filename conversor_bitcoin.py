import requests

def obter_cotacao_bitcoin():
    """Obtém a cotação atual do Bitcoin em Reais da API do CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["brl"]

def converter_bitcoin_para_reais(quantidade_bitcoin, cotacao_bitcoin):
    """Converte uma quantidade de Bitcoins em Reais."""
    return quantidade_bitcoin * cotacao_bitcoin

def converter_reais_para_bitcoin(quantidade_reais, cotacao_bitcoin):
    """Converte uma quantidade de Reais em Bitcoins."""
    return quantidade_reais / cotacao_bitcoin

while True:
    print("\nCONVERSÃO DE CRIPTOMOEDAS")
    print("1 - Converter Bitcoins em Reais")
    print("2 - Converter Reais em Bitcoins")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        try:
            quantidade_bitcoin = float(input("Digite a quantidade de Bitcoins: "))
            cotacao_bitcoin = obter_cotacao_bitcoin()
            reais = converter_bitcoin_para_reais(quantidade_bitcoin, cotacao_bitcoin)
            print(f"{quantidade_bitcoin} Bitcoins equivalem a R$ {reais:.2f}")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    elif opcao == '2':
        try:
            quantidade_reais = float(input("Digite a quantidade de Reais: "))
            cotacao_bitcoin = obter_cotacao_bitcoin()
            bitcoins = converter_reais_para_bitcoin(quantidade_reais, cotacao_bitcoin)
            print(f"R$ {quantidade_reais:.2f} equivalem a {bitcoins:.8f} Bitcoins")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    elif opcao == '3':
        print("Saindo da calculadora...")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
