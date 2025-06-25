# Algoritmo 118
# Geradores - Recuperando dados de uma API

""" 
- Solicitar dados por páginas (paginação)
- Fornecer um produto por vez entre chamadas
- Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas
- Tratar o consumo da API como uma lista Python 
"""

# Exemplo

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1,2,3]):
    print(i)



























# Exemplo 1
#import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1
        
# uso do gerador
""" for product in fetch_products("http://api.example.com/products"):
    print(product['name'])     """   
    

# versão 2

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar API: {response.status_code}")
        
        data = response.json()
        
        for product in data.get('products', []):
            yield product
        
        if 'next_page' not in data:
            break
        
        page += 1

# Uso do gerador
""" for product in fetch_products("http://api.example.com/products"):
    print(product['name']) """
