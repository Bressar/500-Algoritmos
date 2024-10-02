# Algoritmo 54
# Ler um número, dizer se: positivo, negativo ou nulo


def positivo_negativo_nulo():
    while True:
        try:
            numero = float(input("Digite um número: "))
            break
        except ValueError:
            print('Digite um valor válido!')
    if numero > 0:
        print(f'{numero} é positivo.')
    elif numero < 0:
        print(f'{numero} é negativo')
    else:
        print(f'{numero} é nulo.')
        
positivo_negativo_nulo()
