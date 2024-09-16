# Algoritmo 42
# Valores Trocados, a -> b,  b -> a

valor_1 = input('Digite o 1° valor: ')
valor_2 = input('Digite o 2° valor: ')

print(f'1° Valor -> {valor_1} \n'
      f'2° Valor -> {valor_2}')

auxiliar = valor_1
valor_1 = valor_2
valor_2 = auxiliar

print('Valores Trocados')
print(f'1° Valor -> {valor_1} \n'
      f'2° Valor -> {valor_2}')
