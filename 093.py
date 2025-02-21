# Algoritmo 93
# Tabulação à partir dos dados de uma lista de tuplas

# Melhor versão, simplificada, usando uma lista de tuplas (consome menos memória)

# Função otimizada para tabulação
def tabulacao(item1, item2):
    print(f"{item1}\t\t\t{item2}")
    print('--' * 16)

# Lista otimizada com tuplas (mais eficiente que listas)
lista_frutas = [
    (1, 'Limão'),
    (2, 'Maçã'),
    (3, 'Pera'),
    (4, 'Laranja'),
    (5, 'Banana'),
    (6, 'Uva'),
    (7, 'Graviola'),
    (8, 'Jaca'),
    (9, 'Manga'),
    (10, 'Amora')
]

# Função para imprimir a lista com tabulação
def imprimir_tabulacao(lista):
    for numero, fruta in lista:
        tabulacao(numero, fruta)

# Chamando a função com a lista
imprimir_tabulacao(lista_frutas)



print('\n')


# 3 versões anteriores

# Fazendo tabulação
print("zona1", end="")
for a in range(1, 9):  # a varia de 1 a 8 (incluindo 8)
    print("\t", end="")  # Tabulação sem nova linha
print("zona9")  # Imprime zona9 na mesma linha e finaliza corretamente

print('\n')

# usando uma função
def tabulacao(item1, item2):
    print(item1, end="")

    for a in range(1, 4):  # a varia de 1 a 3 (incluindo 3)
        print("\t", end="")  # Tabulação sem nova linha

    print(item2)  # Imprime zona9 na mesma linha e finaliza corretamente
    print('--' * 16)

# uso da função simples
tabulacao(1, 'Limão')
tabulacao(2, 'Maçã')
tabulacao(3, 'Pera')
tabulacao(4, 'Laranja')
tabulacao(5, 'Banana')

print('\n')
# à partir de uma lista
lista_frutas = [
                [6, 'Uva'],
                [7, 'Graviola'],
                [8, 'Jaca'],
                [9, 'Manga'],
                [10, 'Amora']
                ]


def imprimir_tabulacao_de_uma_lista_1(nome_lista):
    for numero, fruta in nome_lista:
        index = numero
        nome_fruta = fruta
        tabulacao(index, nome_fruta)
        

imprimir_tabulacao_de_uma_lista_1(lista_frutas)


print('\n')
# Usando um dicionário
dic_frutas = {
                11 : 'Açaí',
                12 : 'Pitanga',
                13 : 'Siriguela',
                14 : 'Cambuci',
                15 : 'Temóia'
                }

def imprimir_tabulacao_de_uma_lista_2(nome_dicionario):
    for key, value in nome_dicionario.items():
        index = key
        nome_fruta = value
        tabulacao(index, nome_fruta)
        
imprimir_tabulacao_de_uma_lista_2(dic_frutas)
