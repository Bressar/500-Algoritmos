## Algoritmo 005
# Fazer Bolo

def fazer_bolo(roupa_branca=False, tem_bateria=False):
    print('Pegar os ingredientes')         
    if roupa_branca == True:
        print('pegue a batedeira')
    else:
        print('Coloque o avental e pegue a batedeira')
    if tem_bateria == True:
        print('bater os ingredientes na batedeira')
    else:
        print('bater os ingredientes à mão')
    print('- Colocar a massa na forma\n- Colocar a forma no forno\n- Aguardar o tempo necessário\n- Retirar o bolo')
          
fazer_bolo(False, False)
print('\n')
fazer_bolo(True, True)    
    
