# Algoritmo 029
# Bubble Sort - Algoritmo de ordenação de troca - exemplo - Estrutura de dados
""" O Bubble Sort é um algoritmo de ordenação que funciona comparando pares de elementos consecutivos e trocando-os se estiverem fora de ordem. Esse processo é repetido até que a lista esteja ordenada. 
complexidade 𝑂(𝑛²)
"""

aux = 0
vetor= []

tamanho_vetor = int(input('Qual o tamanho do vetor (um número inteiro): '))
#preenche o vetor
for i in range(0, tamanho_vetor):
    numero = int(input('Digite um número: ' ))
    vetor.append(numero)
print(f'Lista: {vetor}') # debug

# se fosse só para ordenar era só usar sorted(), .sort() ou .reverse(), mas é para mostrar o exemplo Bubble Sort
# print(f'Usando a função do Python sorted(): {sorted(vetor)}') 
# vetor.sort()
# print(f'Usando a função do Python sort: {vetor}') 
# vetor.reverse()
# print(f'Usando a função do Python reverse: {vetor}') 

# Bubble Sort Crescente
for i in range(len(vetor)):# Laço externo do tamanho do vetor
    for j in range(0, len(vetor) - i - 1): # laço interno da 1­° até a penúltima posição, não pode ir até a última pq daí não teria 2 elementos para comparar.
        if vetor[j] > vetor[j + 1]:
            # Troca de posições
            aux = vetor[j] # armazena o valor temporariamente
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = aux

print(f'Vetor Resultado crescente: {vetor}')

# Bubble Sort Decrescente
for i in range(len(vetor)):  # Laço externo do tamanho do vetor
    for j in range(0, len(vetor) - i - 1):  # Laço interno da 1ª até a penúltima posição
        if vetor[j] < vetor[j + 1]:  # Troca para ordem decrescente
            # Troca de posições
            aux = vetor[j]  # Armazena o valor temporariamente
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = aux

print(f'Vetor Resultado decrescente: {vetor}')


# Bubble Sort Crescente -> usando while
i = 1
troca = 1

while i <= len(vetor) and troca ==1:
    for j in range(0, len(vetor) - i - 1): # laço interno da 1­° até a penúltima posição
        if vetor[j] > vetor[j + 1]:
            # Troca de posições
            aux = vetor[j] # armazena o valor temporariamente
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = aux

print(f'Vetor Resultado crescente: {vetor}')

""" Ambos os algoritmos têm a mesma complexidade de tempo O(n²) no pior caso.
tanto o os 2 laços for quanto o uso do while + 1 laço for.
A diferença principal é que o Código usando while pode ser mais eficiente em cenários práticos onde a lista pode se tornar ordenada antes de completar todas as iterações. """




# s = {1, 2, 3, 4}
# s.discard(4)
# print(s)