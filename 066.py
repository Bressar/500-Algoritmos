# Algoritmo 66
# Entrar com um verbo no infinitivo e retornar uma das seguintes mensagens:
# verbo não está no infinitivo:
# verbo está na 1ª conjugação
# verbo está na 2ª conjugação
# verbo está na 3ª conjugação


while True:
    print('--' * 20)
    verbo = str(input("Digite um verbo no infinitivo: ")).strip().lower()
        # Verifica se o verbo termina em 'r', ou seja, está no infinitivo
    if verbo.endswith('r'): # método endswith()
        # Pega a penúltima letra para identificar a conjugação
        penultima_letra = verbo[-2]
        
        if penultima_letra == 'a':
            print('Verbo na 1ª conjugação')  # Ex: amar, falar, cantar
        elif penultima_letra == 'e':
            print('Verbo na 2ª conjugação')  # Ex: beber, correr, vender
        elif penultima_letra == 'i':
            print('Verbo na 3ª conjugação')  # Ex: partir, dormir, assistir
        else:
            print('Verbo inválido, não há conjugação com essa terminação: "ur".')
    else:
        print('Não é um verbo no infinitivo')
        
    print('--' * 20)
    sair = input("Pressione qualquer tecla para continuar, ou [S] para sair\n").strip().upper()
    if sair == "S":
        print('--' * 20)
        print("Encerrando o programa...")
        print('--' * 20)
        break


# Primeira versão   
""" verbo = str(input("Digite um verbo: ")).strip()
letra = verbo[-1]

if letra in "Rr":
    n = len(verbo) - 2
    letra = verbo[n]
    
    if letra in "Aa":
        print('Verbo na 1ª conjugação')
        
    elif letra in "Ee" or letra in "Oo":
        print('Verbo na 2ª conjugação')
        
    elif letra in "Ii":
        print('Verbo na 3ª conjugação')
        
    else:
        print('Não existe Verbo com terminação ur')
        
else:
    print('Não é um Verbo no infinitivo')
         """