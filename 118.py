# Algoritmo 118
# Geradores - Recuperando dados de uma API

""" 
- Solicitar dados por páginas (paginação)
- Fornecer um produto por vez entre chamadas
- Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas
- Tratar o consumo da API como uma lista Python 
"""

# Exemplo
""" meu_gerador é uma função que recebe uma lista de números.
Para cada número na lista, ela multiplica o número por 2 e entrega (yield) esse valor.
 """
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2
        
""" yield é uma palavra reservada do Python que transforma uma função comum em um gerador (generator).
Comparando com return:
return encerra a função e entrega um valor de uma vez só.
yield pausa a função, entrega um valor e mantém o estado da função para continuar de onde parou.
Assim, com yield, a função pode continuar de onde parou na próxima iteração.        
 """

for i in meu_gerador(numeros=[1,2,3]):
    print(i)

""" chama a função meu_gerador com [1, 2, 3].
Como a função usa yield, ela retorna um objeto gerador, que é iterado pelo for.
A cada iteração, o gerador:
Executa até o próximo yield.
Retorna numero * 2.
 """

""" Resumo:
yield transforma a função em um gerador.

O gerador produz valores sob demanda, um por vez, de forma eficiente em memória.
 """
























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
