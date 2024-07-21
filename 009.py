# Algoritmo 009
# Leão, cabra e grama
"""
Objetivo: Levar um leão, uma cabra e um pedaço de grama
para o outro lado do rio, o leão nunca pode ficar sozinho com a cabra
e nem a cabra ficar sozinha com o pedaço de grama.
"""

elementos_novos = []

print('--' * 20)
print('''Escolha quem você vai levar para o outro lado rio.
Lembre-se, Na sequência correta!''')
print('--' * 20)

while len(elementos_novos) < 3:
    escolhido = str(input('[L]Leão - [C]Cabra - [G]Grama - [S]Sair -> ')).upper().strip()
    print('--' * 20)
    if escolhido == 'L' and 'Leão' not in elementos_novos:
        elementos_novos.append('Leão')
    elif escolhido == 'C' and 'Cabra' not in elementos_novos:
        elementos_novos.append('Cabra')
    elif escolhido == 'G' and 'Grama' not in elementos_novos:
        elementos_novos.append('Grama')
    elif escolhido == 'S':
        print('Saindo do jogo... :(')
        break
    else:
        print('Valor inválido, escolha novamente!')
        
if elementos_novos[0] == 'Leão' and elementos_novos[1] == 'Cabra':
    print('Perdeu! O Leão come a cabra.')
elif elementos_novos[0] == 'Cabra' and elementos_novos[1] == 'Leão':
    print('Perdeu! O Leão come a cabra.')
elif elementos_novos[0] == 'Cabra' and elementos_novos[1] == 'Grama':
    print('Perdeu! A cabra come a grama.')
elif elementos_novos[0] == 'Grama' and elementos_novos[1] == 'Cabra':
    print('Perdeu! A cabra come a grama.')
elif elementos_novos[0] == 'Grama' and elementos_novos[1] == 'Leão':
    print('Ganhou! O leão não come a grama.')   
elif elementos_novos[0] == 'Leão' and elementos_novos[1] == 'Grama':
    print('Ganhou! O leão não come a grama.')     
     
print(elementos_novos) # for debug
        