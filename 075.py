# Algoritmo 075
# Usando uma funçã lambda, ler o total de pontos de 3 finalistas de um campeonato, e exibir sua colocação final.
# ex: colocação: Nome ->  X pontos

# OBS: ver a versão 075b.py , onde é possível definir qualquer número de competidores

placar = {}

# Entrada dos 3 primeiros colocados, essa versão só tem 3 colocados
for colocacao in range(3):
    nome = input("Nome: ").strip().title()
    while True:
        try:
            pontos = int(input("Números de Pontos: "))
            break # Sai do loop apenas se for um int
        except ValueError:
            print("Por favor, insira um número inteiro para os pontos.")
    placar[nome] = int(pontos) # Armazena o valor apenas após confirmação de entrada válida
        
# Ordena o dicionário pela pontuação em ordem decrescente
placar_ordenado = dict(sorted(placar.items(), key=lambda item: item[1], reverse=True))  

# Explicação dessa linha:
""" 
placar.items() Cria uma tupla para cada chave/item do dicionário,
Exemplo: Se placar fosse {'Alice': 10, 'Bob': 20}, então placar.items() resultaria em [('Alice', 10), ('Bob', 20)].

sorted(..., key=lambda item: item[1], reverse=True):
sorted(...): Ordena a lista de itens do dicionário. Para ordenar de acordo com os valores dos pontos em ordem decrescente), precisamos especificar:
key=lambda item: item[1]: Este é o ponto onde a lambda entra.
reverse=True: Isso indica que queremos a ordem decrescente.

key=lambda item: item[1]:
Lambda é uma maneira de criar uma função anônima (sem nome) em uma única linha.
Aqui, lambda item: item[1] é uma função que diz ao sorted que a chave de ordenação deve ser o segundo elemento de cada item (o valor pontos). Ou seja, vai se basear apenas no item e deixar a chave fora da escolha por ordenação.

Como lambda funciona neste contexto:
lambda item: item[1] significa que para cada item (par chave-valor) que sorted examina, ele deve usar item[1] (o valor pontos) como o critério de ordenação.
Exemplo de aplicação: Se item for ('Alice', 10), então item[1] seria 10, que será usado como critério para ordenar essa entrada.

dict(...):
Após o sorted(...) ordenar a lista de itens (tuplas) com base no valor de pontos, converte essa lista ordenada de volta para um dicionário usando dict(...). Isso gera um novo dicionário, placar_ordenado, onde os itens estão organizados na ordem desejada.
 """

print('--' * 30)
print("\nCLASSIFICAÇÂO FINAL:")
posicao = 0
for nome, pontos in placar_ordenado.items():
    posicao += 1
    print(f'{posicao}ª Posição: {nome} -> {pontos} pontos')
print('--' * 30)    
