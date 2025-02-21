# Algoritmo 93

# Tabulação à partir dos dados de uma lista

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


def imprimir_tabulacao_de_uma_lista(nome_lista):
    for numero, fruta in nome_lista:
        index = numero
        nome_fruta = fruta
        tabulacao(index, nome_fruta)
        

imprimir_tabulacao_de_uma_lista(lista_frutas)
