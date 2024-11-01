# Algoritmo 076
# Criar uma equipe de 3 jogadores
# ler os pontos de cada jogadr da equipe e exibir em ordem decrescente
# Se a soma dos 3 jogadores for > que 100, exibir média e acrescentar no ranking de equipes
# se for < 100 -> equipe desclassicada
# apresentar ranking final

# OBSERVAÇÃO: Tá tudo feito em linguagem Estruturada, mas seria melhor em POO...

def criar_equipe(nome_da_equipe= "Nome da equipe"):
    equipe = {} 
    for i in range(3): # Lê os nomes e pontos dos jogadores 3X
        print('--' * 30)
        nome = input("Digite o nome do jogador: ").strip().title()
        while True:
            try:
                print('--' * 30)
                pontos = int(input("Digite o número de pontos: "))
                break
            except ValueError as e:
                print(f'{e} - Digite um número inteiro')
                print('--' * 30)
        equipe[nome] = pontos          
    # Ordena a equipe em ordem decrescente de pontos
    equipe_ordenada = dict(sorted(equipe.items(), key=lambda item: item[1], reverse=True))  
    # Calcula a soma dos pontos da equipe
    total_pontos_equipes = sum(equipe_ordenada.values())    
    return nome_da_equipe, equipe_ordenada, total_pontos_equipes


# Lista para armazenar equipes classificadas
ranking_de_equipes = []


def exibir_ranking_equipes(ranking):
    # Ordena o ranking pela média de pontos em ordem decrescente
    ranking_ordenado = sorted(ranking, key=lambda x: x['media'], reverse=True)

    print('--' * 40)
    print("\nRanking Final das Equipes Classificadas:")
    for posicao, equipe_info in enumerate(ranking_ordenado, start=1):
        print('--' * 40)
        print(f"{posicao}º - Equipe: {equipe_info['nome']} | Média: {equipe_info['media']:.2f} pontos | Total: {equipe_info['total']} pontos\n{equipe_info['equipe']}")
        print('--' * 40)

# Criação de equipes e adição ao ranking
while True: # Pode ajustar a quantidade de equipes desejadas
    try:
        quantidade_equipes = int(input("Defina o número de equipes na competição: ")) 
        break
    except ValueError:
        print("ERRO! Digite um número válido!")
            
for _ in range(quantidade_equipes):  
    print('--' * 30)
    nome_da_equipe = input("Digite o nome da equipe: ").strip().title()
    nome_da_equipe, equipe, total_pontos_equipe = criar_equipe(nome_da_equipe)

# Verifica se a equipe está classificada
    if total_pontos_equipe > 100:
        media_pontos_equipe = total_pontos_equipe / len(equipe)
        ranking_de_equipes.append({
            'nome': nome_da_equipe,
            'equipe': equipe,
            'media': media_pontos_equipe,
            'total': total_pontos_equipe
        })
        print(f"\nEquipe CLASSIFICADA! Média de pontos: {media_pontos_equipe:.2f}")
    else:
        print("\nEquipe DESCLASSIFICADA!")

# Exibe o ranking final das equipes classificadas em ordem decrescente de média de pontos
if ranking_de_equipes:
    exibir_ranking_equipes(ranking_de_equipes)
else:
    print("Nenhuma equipe foi classificada.")








# versão 1
# cria equipe com 3 competidoes e seus pontos
""" def criar_equipe(nome_da_equipa= "Nome da equipa"):
    equipe = {} 
    # Lê os nomes e pontos dos jogadores
    for i in range(3): 
        nome = input("Digite o nome do jogador: ").strip().title()
        while True:
            try:
                pontos = int(input("Digite o número mos de pontos: "))
                break
            except ValueError as e:
                print(f'{e} - Digite um número inteiro')
        equipe[nome] = pontos
        
    # Ordena a equipe em ordem decrescente de pontos
    equipe_ordenada = dict(sorted(equipe.items(), key=lambda item: item[1], reverse=True))
    
    # Calcula a soma dos pontos da equipe
    total_pontos_equipes = sum(equipe_ordenada.values())
    
    return nome_da_equipa, equipe_ordenada, total_pontos_equipes

# criando equipe e recebendo os dados
nome_da_equipa, equipe1, total_pontos_equipe1 = criar_equipe(nome_da_equipa="Equipe 1")

# apresenta a equipe ordenada
print('--' * 30)
print(f'Team: {nome_da_equipa}')
print('--' * 30)
print("Ranking de Pontos:")
for nome, pontos in equipe1.items():
    print(f'{nome}: {pontos} pontos')
print('--' * 30)    
# Apresenta a soma de todos os pontos da equipe
print(f'Soma total dos pontos da equipe: {total_pontos_equipe1}')
print('--' * 30)

ranking_de_equipes = []

if total_pontos_equipe1 > 100:
    ranking_de_equipes.append(equipe1)
    media_pontos_equipe = total_pontos_equipe1 / 3 # ou len(equipe_ordenada)
    print(f"\nEquipe CALSSIFICADA! Média de pontos: {media_pontos_equipe} pontos")
else:
    print("\nEquipe ELIMINADA!!")
    
for equipe in ranking_de_equipes:
    print(equipe, end="\n")
    
     """