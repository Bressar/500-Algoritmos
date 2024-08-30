# Algoritmo 031
# Quick Sort - Algoritmo de ordenação rápida

""" Com base no pivô e considerando uma ordenação crescente, o algoritmo
compara todos os valores que estão à esquerda dele, verificado se eles são
menores que o pivô. Em seguida, são comparados todos os valores que estão à
direita do pivô, verificando se eles são maiores que o valor de referência do pivô.
Sempre que um valor maior que o pivô é encontrado do lado esquerdo e/ou um
valor menor é achado do lado direito, ambos trocam de posição (swap). 
complexidade 𝑂(𝑛²)
"""


vetor = [6, 1, 8, 2, 7]

def troca(x, i, j):
    # Troca os elementos de posição i e j
    aux = x[i]
    x[i] = x[j]
    x[j] = aux

def particao(x, inicio, fim):
 # Escolhe o elemento do meio como pivô
    meio = (inicio + fim) // 2
    pivo = x[meio]
    # Coloca o pivô na posição inicial temporariamente
    troca(x, inicio, meio)
    i = inicio + 1
    j = fim

    while True:
        # Encontra o primeiro elemento à direita que é menor ou igual ao pivô
        while i <= j and x[i] <= pivo:
            i += 1
        # Encontra o primeiro elemento à esquerda que é maior ou igual ao pivô
        while i <= j and x[j] >= pivo:
            j -= 1
        if i <= j:
            # Troca elementos incoerentes
            troca(x, i, j)
        else:
            # Coloca o pivô na posição correta
            troca(x, inicio, j)
            return j

# Quick sort crescente
def quick_sort(x, inicio=0, fim=None):
    if fim is None:
        fim = len(x) - 1

    if inicio < fim:
        div = particao(x, inicio, fim)  # Particiona o vetor
        quick_sort(x, inicio, div - 1)  # Ordena a primeira metade
        quick_sort(x, div + 1, fim)  # Ordena a segunda metade

# Ordena o vetor
quick_sort(vetor)

# Imprime o vetor ordenado
for i in range(len(vetor)):
    print(vetor[i], end=' ')
