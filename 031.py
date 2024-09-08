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

def troca(vetor, i, j):
    # Troca os elementos de posição i e j
    aux = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = aux

def particao(vetor, inicio, fim):
    # Escolhe o elemento do meio como pivô
    meio = (inicio + fim) // 2
    pivo = vetor[meio]
    # Coloca o pivô na posição inicial temporariamente
    troca(vetor, inicio, meio)
    i = inicio + 1
    j = fim

    while True:
        # Encontra o primeiro elemento à direita que é menor ou igual ao pivô
        while i <= j and vetor[i] <= pivo:
            i += 1
        # Encontra o primeiro elemento à esquerda que é maior ou igual ao pivô
        while i <= j and vetor[j] >= pivo:
            j -= 1
        if i <= j:
            # Troca elementos incoerentes
            troca(vetor, i, j)
        else:
            # Coloca o pivô na posição correta
            troca(vetor, inicio, j)
            return j

# Quick sort crescente
def quick_sort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1

    if inicio < fim:
        div = particao(vetor, inicio, fim)  # Particiona o vetor
        quick_sort(vetor, inicio, div - 1)  # Ordena a primeira metade
        quick_sort(vetor, div + 1, fim)  # Ordena a segunda metade

# Ordena o vetor
quick_sort(vetor)

# Imprime o vetor ordenado
for i in range(len(vetor)):
    print(vetor[i], end=' ')
