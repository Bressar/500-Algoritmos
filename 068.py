# Algoritmo 68
# Conversor de moedas -> usando uma API para ter o câmbio atualizado

# Precisa se cadastar para ter uma chave de acesso, a API Key!! Usei essa: https://app.exchangerate-api.com/

import requests
API_KEY = 'd02fbaba7760b03e7bc655f4'
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"  # URL da API
response = requests.get(URL) # Fazendo a requisição para a API

# Verificando se a requisição foi bem sucedida (status code 200)
if response.status_code == 200:
    # Convertendo a resposta para JSON
    data = response.json()  
    # Exibindo toda a resposta para entender a estrutura
    # print("Resposta completa da API:", data) # for debug

 # Acessando as taxas de câmbio (conversion_rates)
    if 'conversion_rates' in data:
        rates = data['conversion_rates']
    else:
        print("A resposta não contém as taxas de câmbio esperadas.")
        exit(1)
else:
    print(f"Erro na requisição: {response.status_code}")
    exit(1)

# # Exibindo as cotações específicas for debug
# print("Cotação das moedas:")
# print(f"USD para BRL: {rates.get('BRL', 'Não disponível')}")
# print(f"USD para EUR: {rates.get('EUR', 'Não disponível')}")
# print(f"USD para GBP: {rates.get('GBP', 'Não disponível')}")


def converter_moeda(valor, taxa_origem, taxa_destino):
    return valor * (taxa_destino / taxa_origem)


# Mapeamento das opções de moedas para facilitar a escolha
opcoes_moedas = {
    'R': 'BRL',
    'D': 'USD',
    'E': 'EUR'
}

while True:
    print('--' * 20)
    try:   
        valor_conversao = float(input("Digite o valor a ser convertido: "))
        break
    except ValueError:
        print("Valor inválido! Digite novamente!")
while True:        
    moeda_inicial = input("Coverter de:\n[R] Real, [D] Dolar - [E] Euro\n").strip().upper()
    if moeda_inicial in opcoes_moedas:
        moeda_inicial_codigo = opcoes_moedas[moeda_inicial]
        break
    else:
        print("Erro! escolha inválida!")       
while True:
    moeda_final = input("Para:\n[R] Real, [D] Dolar - [E] Euro\n").strip().upper()
    if moeda_final in opcoes_moedas:
        moeda_final_codigo = opcoes_moedas[moeda_final]
        break
    else:
        print("Erro! escolha inválida!")
        
# Conversão usando as taxas fornecidas pela API
if moeda_inicial_codigo == "USD":
    taxa_origem = 1  # Dólar é a moeda base da API
else:
    taxa_origem = rates.get(moeda_inicial_codigo, None)

if moeda_final_codigo == "USD":
    taxa_destino = 1  # Dólar é a moeda base da API
else:
    taxa_destino = rates.get(moeda_final_codigo, None)

if taxa_origem is None or taxa_destino is None:
    print('--' * 20)
    print(f"Erro ao obter a taxa de câmbio para {moeda_inicial_codigo} ou {moeda_final_codigo}.")
    print('--' * 20)
else:
    valor_convertido = converter_moeda(valor_conversao, taxa_origem, taxa_destino)
    print('--' * 20)
    print(f"{valor_conversao:.2f} {moeda_inicial_codigo} equivalem a {valor_convertido:.2f} {moeda_final_codigo}")
    print('--' * 20)
    