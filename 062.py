# Algoritmo 62
# Reconhecendo a primeira letra de um nome e organizando uma lista de nomes em ordem alfabética

# Reconhecer se um nome começa com a letra A
# palavra = input("Escreva uma palavra: ") 
# if palavra[0] in 'aA':
#     print(f'A palavra {palavra} começa com a letra A')
# else:
#     print(f'A palavra {palavra} começa com a letra {palavra[0]}')
    
    
lista_nomes = []  
 
while True:   
    nome = input('Escreva um nome: ').strip().title()
    lista_nomes.append(nome)
    print('--' * 20)
    print(f'O nome {nome} começa com a letra {nome[0]}')
    print('--' * 20)
        
    print('--' * 20)
    sair = input("Pressione qualquer tecla para continuar\nPara sair pressione [S]\n").upper().strip()
    if sair == "S":
        print('--' * 20)
        print('Encerrando o programa...')
        print('--' * 20)
        break
    else:
        continue
    
print('--' * 20)
print(f'Lista de nomes em ordem alfabética:')
for nome in sorted(lista_nomes):
    print('->', nome)
print('--' * 20)
