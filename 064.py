# Algoritmo 64, 

# Insert Sort (ordenando o array em ordem crescente)

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            # Troca os elementos de posição
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

# Exemplo de uso:
arr = [5, 2, 4, 6, 1, 3]
insertion_sort(arr)
print("Array ordenado:", arr)
