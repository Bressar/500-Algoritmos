# Algoritmo 010
# Missionários e Canibais
print(
    '''
Levar 3 missionários e 3 canibais de um lado para outro do rio,
margem A e margem B, com um bote, nunca pode haver mais missionários
do que canibais, senão os missionários catequizam os canibais,
como fazer para levar os 6 de uma margem para outra?
No bote, além de você, só podem ir 2 pessoas.
'''
)
margem_rio_A = ['canibal', 'canibal', 'canibal',
                'missionário', 'missionário', 'missionário']
margem_rio_B = []
bote = []
quant_missionarios_A = 3
quant_missionarios_B = 0
quant_canibais_A = 3
quant_canibais_B = 0

while True:
    # Escolha de quantos vão no bote
    if 'missionário' in margem_rio_A:
        n_missionarios = int(input('Quantos missionarios você quer levar no bote? '))
        if  -1 < n_missionarios < 3 and len(bote) <= 2 and quant_missionarios_A >= n_missionarios:
                for i in range (n_missionarios):
                    bote.append('missionário')
                    margem_rio_A.remove('missionário')
                quant_missionarios_A = margem_rio_A.count('missionário')
                quant_missionarios_B = margem_rio_B.count('missionário')
        else:
            print('Valor inválido, tente novamente!')
            continue

    if 'canibal' in margem_rio_A and len(bote) < 2:      
            n_canibais = int(input('Quantos canibais você quer levar no bote? '))
            if  -1 < n_canibais < 3 and len(bote) <= 2 and quant_canibais_A >= n_canibais:
                    for i in range (n_canibais):
                        bote.append('canibal')
                        margem_rio_A.remove('canibal')
                    quant_canibais_A = margem_rio_A.count('canibal')
                    quant_canibais_B = margem_rio_B.count('canibal')
            else:
                print('Valor inválido, tente novamente!')
                continue 
    
    print('---' * 20)
    # quantos ficam na margem B
    if 'missionário' in bote:
            n_missionarios = int(input('Quantos missionarios você quer deixar na margem B? '))
            if  -1 < n_missionarios < 3:
                    for i in range (n_missionarios):
                        margem_rio_B.append('missionário')
                        bote.remove('missionário')
                    quant_missionarios_A = margem_rio_A.count('missionário')
                    quant_missionarios_B = margem_rio_B.count('missionário')
            else:
                print('Valor inválido, tente novamente!')
                continue 
        
    if 'canibal' in bote:   
            n_canibais = int(input('Quantos canibais você quer deixar na margem B? '))
            if  -1 < n_canibais < 3:
                    for i in range (n_canibais):
                        margem_rio_B.append('canibal')
                        bote.remove('canibal')
                    quant_canibais_A = margem_rio_A.count('canibal')
                    quant_canibais_B = margem_rio_B.count('canibal')
            else:
                print('Valor inválido, tente novamente!')
                continue
            
    print('\n')       
    print('---' * 20)             
    print(f'''Quem está na margem A: {margem_rio_A}''')  
    print('---' * 20)    
    print(f'Quem está no bote: {bote}')
    print('---' * 20) 
    print(f'''Quem está na margem B: {margem_rio_B}''')
    print('---' * 20)
    print('\n')    
    
  # and (quant_canibais_B != 0 and quant_missionarios_B != 0) and (quant_missionarios_B > quant_canibais_B  
    if (quant_missionarios_B > quant_canibais_B) and quant_canibais_B > 0: 
        print('Fim de jogo! os missionários catequizaram os canibais...')
        print(" *- RODOU! -* " * 5)
        break       
    elif margem_rio_B.count('canibal') == 3 and  margem_rio_B.count('missionário') == 3:
        print('Você venceu! Conseguiu passar todos para a outra margem do rio!')
        print(" *- GANHOU! -* " * 5)
        break
     

# for debug
# print(quant_missionarios_A)
# print(quant_missionarios_B)
# print(quant_canibais_A)
# print(quant_canibais_B)

