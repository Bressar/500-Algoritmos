# Algoritmo 007
# Jogo da Forca

def jogo_da_forca(palavra_secreta='palavra'):
    print('Jogo da Forca')
    palavra_secreta = palavra_secreta.strip().upper()
    lista_palavra_secreta = list(palavra_secreta)

    lista_exibicao = []
    for letra in lista_palavra_secreta:
        lista_exibicao.append("*")
    for item in lista_exibicao:
            print(item, end= '')

    erros = 0

    while True:
        if lista_palavra_secreta == lista_exibicao:
            print('\nVocê ganhou! Saindo do jogo...')
            break
        
        letra_escolhida = input('\nescolha uma letra: ').strip().upper()
        if letra_escolhida in lista_palavra_secreta:
            for index, letra in enumerate(lista_palavra_secreta): # enumerate para pegar todas as letras iguais
                if letra == letra_escolhida:
                    lista_exibicao[index] = letra_escolhida

            for item in lista_exibicao:
                print(item, end= '')
            #print(lista_exibicao)
        else:
            erros += 1
            print(f'A letra [{letra_escolhida}] não está na palavra!')
            
        if erros >= 7:
            print('\nVocê perdeu! Saindo do jogo...')
            break
            
jogo_da_forca('banana')

