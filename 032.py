# Algoritmo 032
# Algoritmo de busca 

#busca sequêncial -> complexidade 𝑂(𝑛) - exemplos da aula de estrutura de dados

#import random

# Valores não ordenados
buscado = 34
vetor = [6, 1, 8, 2, 7, 10, 34, 0]

# Easy way in Python!! 2 linhas
# if buscado in vetor:
#     print("Número encontrado!")

for i in range (len(vetor)): # busca sequencial
    print(f"posição {i} = {vetor[i]}")
    if vetor[i] == buscado:
        print(f"Valor encontrado na posição:  {i}")
        break
    else:
        print("Valor não encontrado")
        

# Valores ordenados - > complexidade 𝑂(𝑛) - forma ilustrativa (não o melhor código de python)
buscado = int(input("Escolha um número de 1 a 10: "))
achou = 0
# numeros = list(random.sample(range(1, 100), 10)) # gera uma lista de 10 númeos aleatórios entre 1 e 99
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
tamanho_do_vetor = len(x)

while i <= tamanho_do_vetor and achou == 0 and buscado >= x[i]:
    if x[i] == buscado:
        achou = 1
    else:
        i += 1
    if achou == 0:
        print(f"Valor NÃO encontrado na posição: {i}")
    else:
        print(f"Valor encontrado na posição: {i + 1}" )
        
       
# Busca Binária - > complexidade 𝑂(𝑙𝑜𝑔𝑛) - só funciona com o vetor ordenado
buscado = int(input("Escolha um número: "))

x = [i for i in range(1, 11)] # lista de 1 a 10
inicio = 0
fim = len(x) - 1
achou = 0

while inicio <= fim and achou == 0:
    meio = (inicio + fim) // 2  # Cálculo de 'meio' dentro do loop
        
    if x[meio] == buscado:
        achou = 1 
    else:
        if buscado < x[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
                                 
if achou == 0:
    print("Valor não encontrado!")
else:
    print(f"Valor encontrado na posição {meio}")
        




        