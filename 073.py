# Algoritmo 73
# Usando uma API para consultar dados de clima de uma cidade e determinar se o tempo está favorável para uma atividade externa

# Se houver cidades com o mesmo nome ele vai bugar, poderia ser implementado um sistema que no caso de duplicidade de nomes, fossem pedidas a latidude e a longitude da cidade, mas isso é só um exercício simples, fica pra um trampo 'profissinal'

# https://openweathermap.org/api # -> fazer o cadastro nesse endereço

import requests

API_KEY = '9187de882145c2ecbc93eae365834885'
URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    print('--' * 32)
    cidade = input("Digite o nome de uma CIDADE para saber as condições climáticas:\n").strip()
    pais = input("Digite o código do PAÍS (exemplo: BR para Brasil, US para EUA):\n").strip()

    # parâmetros da requisição da API
    params ={
        'q': f"{cidade},{pais}",  # Inclui o código do país no nome da cidade
        'appid': API_KEY,
        'units': 'metric', # temperatura em Celsius
        'lang' : 'pt_br' # idioma
    }
    # Requisição para API
    response = requests.get(URL, params=params)

    #Verificar se a requisição foi bem sucedida
    if response.status_code == 200:
        dados = response.json() # recebe os dados em json
        # Extrai os dados das informações climáticas
        temperatura = dados['main']['temp']
        descricao_clima = dados['weather'][0]['description']
        chance_de_chuva = dados.get('rain', {}).get('1h', 0)  # Chuva na última hora (mm)
        print('--' * 32)
        print(f"Clima atual em {cidade.title()}, {pais.upper()}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Descrição: {descricao_clima}")
        print(f"Chance de chuva (última hora): {chance_de_chuva} mm")
        print('--' * 32)
        # Condições para um evento ao ar livre
        if chance_de_chuva < 2 and temperatura >= 15 and temperatura <= 32:
            print(f"Em {cidade.title()}, o clima está favorável para atividades ao ar livre!")
            print('--' * 35)
            break
        else:
            print(f"Em {cidade.title()}, o clima pode não estar ideal para atividades ao ar livre!")
            print('--' * 35)
            break

    else:
        print("Não foi possível obter dados climáticos para a cidade informada.")
        print(f"Erro {response.status_code}: {response.json()}") # exibição do erro
"""Exibição de Erros:
Se a API retornar uma resposta diferente de 200 (o que significa que a requisição falhou), o programa exibirá o código de status e a mensagem de erro detalhada fornecida pela API.
Possíveis Problemas:
401 Unauthorized: A API_KEY pode estar incorreta ou inativa.
404 Not Found: O nome da cidade pode estar incorreto. Certifique-se de digitar o nome completo e corretamente. """

    
#print(f'!for debug!\nTodas as informações fornecidas pela API:\n {dados}') # todas as informações fornecidas pela api, for debug
# print(f'!for debug!\nTodas as informações fornecidas pela API:')
# for descricao, codigo in dados.items():
#         print(f'{descricao} -> {codigo}')


# Dicionário com todos os códigos de países do mundo
codigos_paises = {
    'Afeganistão': 'AF',
    'África do Sul': 'ZA',
    'Albânia': 'AL',
    'Alemanha': 'DE',
    'Andorra': 'AD',
    'Angola': 'AO',
    'Arábia Saudita': 'SA',
    'Argentina': 'AR',
    'Armênia': 'AM',
    'Austrália': 'AU',
    'Áustria': 'AT',
    'Azerbaijão': 'AZ',
    'Bahamas': 'BS',
    'Bangladesh': 'BD',
    'Barbados': 'BB',
    'Bélgica': 'BE',
    'Belize': 'BZ',
    'Benin': 'BJ',
    'Bolívia': 'BO',
    'Brasil': 'BR',
    'Bulgária': 'BG',
    'Burkina Faso': 'BF',
    'Cabo Verde': 'CV',
    'Camboja': 'KH',
    'Camarões': 'CM',
    'Canadá': 'CA',
    'Catar': 'QA',
    'Chile': 'CL',
    'China': 'CN',
    'Colômbia': 'CO',
    'Coreia do Norte': 'KP',
    'Coreia do Sul': 'KR',
    'Costa do Marfim': 'CI',
    'Costa Rica': 'CR',
    'Croácia': 'HR',
    'Cuba': 'CU',
    'Dinamarca': 'DK',
    'Egito': 'EG',
    'Emirados Árabes Unidos': 'AE',
    'Equador': 'EC',
    'Eslováquia': 'SK',
    'Eslovênia': 'SI',
    'Espanha': 'ES',
    'Estados Unidos': 'US',
    'Estônia': 'EE',
    'Etiópia': 'ET',
    'Filipinas': 'PH',
    'Finlândia': 'FI',
    'França': 'FR',
    'Gabão': 'GA',
    'Gana': 'GH',
    'Geórgia': 'GE',
    'Grécia': 'GR',
    'Guatemala': 'GT',
    'Guiné': 'GN',
    'Haiti': 'HT',
    'Honduras': 'HN',
    'Hungria': 'HU',
    'Índia': 'IN',
    'Indonésia': 'ID',
    'Irã': 'IR',
    'Iraque': 'IQ',
    'Irlanda': 'IE',
    'Islândia': 'IS',
    'Israel': 'IL',
    'Itália': 'IT',
    'Jamaica': 'JM',
    'Japão': 'JP',
    'Jordânia': 'JO',
    'Kazakhstan': 'KZ',
    'Quênia': 'KE',
    'Laos': 'LA',
    'Letônia': 'LV',
    'Líbano': 'LB',
    'Líbia': 'LY',
    'Lituânia': 'LT',
    'Luxemburgo': 'LU',
    'Macedônia': 'MK',
    'Madagascar': 'MG',
    'Malásia': 'MY',
    'Maldivas': 'MV',
    'Mali': 'ML',
    'Malta': 'MT',
    'Marrocos': 'MA',
    'México': 'MX',
    'Moldávia': 'MD',
    'Mônaco': 'MC',
    'Mongólia': 'MN',
    'Montenegro': 'ME',
    'Moçambique': 'MZ',
    'Namíbia': 'NA',
    'Nepal': 'NP',
    'Nicarágua': 'NI',
    'Nigéria': 'NG',
    'Noruega': 'NO',
    'Nova Zelândia': 'NZ',
    'Omã': 'OM',
    'Países Baixos': 'NL',
    'Paquistão': 'PK',
    'Panamá': 'PA',
    'Paraguai': 'PY',
    'Peru': 'PE',
    'Polônia': 'PL',
    'Portugal': 'PT',
    'Reino Unido': 'GB',
    'República Dominicana': 'DO',
    'República Tcheca': 'CZ',
    'Romênia': 'RO',
    'Rússia': 'RU',
    'Senegal': 'SN',
    'Sérvia': 'RS',
    'Singapura': 'SG',
    'Síria': 'SY',
    'Sri Lanka': 'LK',
    'Suécia': 'SE',
    'Suíça': 'CH',
    'Suriname': 'SR',
    'Tailândia': 'TH',
    'Tanzânia': 'TZ',
    'Togo': 'TG',
    'Trinidad e Tobago': 'TT',
    'Tunísia': 'TN',
    'Turquia': 'TR',
    'Ucrânia': 'UA',
    'Uganda': 'UG',
    'Uruguai': 'UY',
    'Uzbequistão': 'UZ',
    'Vaticano': 'VA',
    'Venezuela': 'VE',
    'Vietnã': 'VN',
    'Zâmbia': 'ZM',
    'Zimbábue': 'ZW'
}







# Não consegui uma api confiável para fazer o código abaixo....

# Ler o nome de um município, n° de eleitores aptos, n° de votos do candidato mais votado, e dizer se ele estará no 2° turno. 
# Usando API do IBGE - não cnsegui acessar aqui de PT... 
# Só municípios com mais de 20000 eleitores tem 2° turno

""" 
import  requests
API_KEY = ''
URL = f" "

response = requests.get(URL)
nome_municipio = input('Nome do Município: ').strip()
eleitores_aptos = 0
numero_de_votos = 0

if eleitores_aptos > 20000 and numero_de_votos <= (numero_de_votos / 2):
    print(f'Em {nome_municipio} haverá 2° Turno')
else:
    print(f'Em {nome_municipio} NÃO haverá 2° Turno') """

