# Algoritmo 030
# Merge Sort - Algoritmo de ordenação por intercalação 

vetor = []

tamanho_vetor = int(input('Qual o tamanho do vetor (um número inteiro): '))
# Preenche o vetor
for i in range(0, tamanho_vetor):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

def intercala(x, inicio, fim, meio):  
    inicio_vetor1 = inicio
    inicio_vetor2 = meio + 1
    poslivre = inicio  
    aux = [0] * (fim - inicio + 1) # cria uma lista de tamanho correto

    # Intercala os dois subvetores
    while inicio_vetor1 <= meio and inicio_vetor2 <= fim:
        if x[inicio_vetor1] <= x[inicio_vetor2]:
            aux[poslivre - inicio] = x[inicio_vetor1]
            inicio_vetor1 += 1
        else:
            aux[poslivre - inicio] = x[inicio_vetor2]
            inicio_vetor2 += 1
        poslivre += 1

    # Se houver ainda números no primeiro subvetor que não foram intercalados
    while inicio_vetor1 <= meio:
        aux[poslivre - inicio] = x[inicio_vetor1]
        inicio_vetor1 += 1
        poslivre += 1

    # Se ainda existir números no segundo subvetor que não foram intercalados  
    while inicio_vetor2 <= fim:
        aux[poslivre - inicio] = x[inicio_vetor2]
        inicio_vetor2 += 1
        poslivre += 1

    # Retorna os valores para o vetor original `x`
    for i in range(inicio, fim + 1):
        x[i] = aux[i - inicio]

def merge(x, inicio=0, fim=None):
    if fim is None:  # Define `fim` como o último índice do vetor
        fim = len(x) - 1  # o fim é -1 para poder haver um elemento de comparação, (uma dupla)
    if inicio < fim:
        meio = (inicio + fim) // 2  # Calcula o meio usando divisão inteira
        merge(x, inicio, meio)  # Ordena a primeira metade
        merge(x, meio + 1, fim)  # Ordena a segunda metade
        intercala(x, inicio, fim, meio)  # Intercala as duas metades

merge(vetor)  # Chama a função `merge` com o vetor

print(f'Vetor Resultado crescente: {vetor}')  # Imprime o vetor ordenado

