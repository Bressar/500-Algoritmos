# Algoritmo 013
# Entrar com uma número no formato CDU e imprimir invertido UDC:

# versão 1 - usando inteiros
while True:
    try:
        numero = int(input('Digite um número de 3 digitos: '))
        if numero < 100 or numero > 999:
            print('Erro! o número não tem 3 casas decimais')
        else:
            centena = numero // 100
            dezena = (numero % 100 ) // 10
            unidade = numero % 10
            numero_invertido = str(unidade)+str(dezena)+str(centena)# versão criando uma variável
            print(f'Número invertido: {numero_invertido}')
            #print(f'Número invertido: {unidade}{dezena}{centena}') # versão direta
            break
    except ValueError:
        print('Valor inválido, tente novamente!')


# versão 2 - usando strings
while True:
    numero_string = input('Digite um número de 3 digitos: ').strip()
    if len(numero_string) == 3 and numero_string.isdigit():
        centena = numero_string[:1]
        dezena = numero_string[1:2]
        unidade = numero_string[-1]
        numero_invertido = unidade + dezena + centena# versão criando uma variável
        print(f'Número invertido: {numero_invertido}')
        # print(f'Número invertido: {unidade}{dezena}{centena}')
        break
    else:
        print('Valor inválido!')
 
    
 # versão 3 - usando uma lista
while True:
    try:
        numero = int(input('Digite um número de 3 digitos: '))
        if numero < 100 or numero > 999:
            print('Erro! o número não tem 3 digitos')
        else:
            numero_string = str(numero)
            numero_lista = []
            for char in numero_string:
                numero_lista.append(int(char))
            numero_lista.reverse()
            #numero_lista.sort(reverse=True) # outra possibilidade
            print('Número invertido: ', end='')
            for numero in numero_lista:
                print(numero, end='')
            # for item in range(len(numero_lista)): # versão complicando tudo...
            #     print(numero_lista[item], end='')
            break
    except:
        print('Valor inválido, tente novamente!')
            
