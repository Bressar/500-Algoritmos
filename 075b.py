# Algoritmo 075 - B version
# Usando uma funçã lambda, ler o total de pontos de X competidores e exibir sua colocação final. ex: colocação: Nome ->  X pontos

placar = {}

while True:
    print('--' * 30)
    nome = input("Nome: ").strip().title()
    while True:
        try:
            pontos = int(input("Números de Pontos: "))
            break 
        except ValueError:
            print("Por favor, insira um número inteiro para os pontos.")
    placar[nome] = int(pontos)
    sair = input("[C] Continuar - [S] Sair ").strip().upper()
    if sair == "S":
        print("Encerrando o programa...")
        break      
# Ordena o dicionário pela pontuação em ordem decrescente
placar_ordenado = dict(sorted(placar.items(), key=lambda item: item[1], reverse=True)) 
 
# Exibição do resultado
print('--' * 30)
print("CLASSIFICAÇÃO FINAL:")
posicao = 0
for nome, pontos in placar_ordenado.items():
    posicao += 1
    print(f'{posicao}ª Posição: {nome} -> {pontos} pontos')
print('--' * 30)    
