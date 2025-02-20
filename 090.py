# Algoritmo 90

# Se uma palavra começar com L ou D, formar um palavra que terá os 2 primeiros carcteres e o último.
# Caso contrário, a palavra será formada por todos os caracteres menos o primeiro.

while True:
    palavra = input('Escreva uma palavra:\n').strip().capitalize()

    if len(palavra) > 3:
        if palavra.startswith('L') or palavra.startswith('D'):
            palavra_1 = palavra[2:-1]
            break
        else:
            palavra_1 = palavra[1:]
            break
    else:
        print('Palavra muito pequena, tente novamente')
        #exit()
        
print(palavra_1)

