# Algoritmo 92
# 3 algoritmos de estrutura de repetição (laço 'for')

print('Python'.upper())

print('---' * 20)
# Volta na lagoa + abdominais, para cada 3 voltas , 5 addominais
volta_lagoa, abdominais = 0, 0

for volta in range (1, 4):
    volta_lagoa += 1
    print(f'{volta}° volta')
    for abominal in range(1,6):
        abdominais += 1
        print(f'{abominal} - Abdominal')
    print('-*-*-' * 3)


print('---' * 20)
# Criar um algoritmo que imprima todos os números pares de 1-10
for numero in range (1,11):
    if numero % 2 == 0:
        print(numero)


print('---' * 20)
# Entrar com 5 números e imprimir o quadrado de cada 1
for pergunta in range(5):
    try:
        numero = int(input('Digite um número para saber o seu quadrado: '))
        print(f'O quadrado de {numero} é:', numero ** 2)
    except ValueError:
        print('Valor inválido! Try again!')
    
    