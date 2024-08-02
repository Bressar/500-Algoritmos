# Algoritmo 015
# Processador de números

line = input("Digite uma sequência de números - separados com espaços: ")
strings = line.split() # transforma em uma lista de item, eliminado assim os espaços
total = 0

# print(strings)

try:
    for substr in strings: # para cada item na lista
        total += float(substr) # converte de string para float e soma no contador 'total'
    print("O total é:", total)
except:
    print(substr, "não é um número.")
    