## Algoritmo 006
# Fazer uma prova

def fazer_prova(tempo=None):
    print('Ler a prova\nPegar caneta')
    questions = True #'em_branco'
    
    while questions and  (tempo is None or -1 < tempo <= 61):
        resposta = input('Sabe a questão [S][N]? ').strip()
        if resposta in 'Ss':
            print('Responda')
            questions = False
        else:
            print('pule para a próxima')
            
        # Atualize o tempo se necessário
        #if tempo is not None:
         #   tempo -= 1    
            
    print('Entregar a prova')
         
fazer_prova()
