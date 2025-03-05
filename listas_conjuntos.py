# Lista e matrizes

""" matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]   
]
print(matriz[0][-1])
print(matriz[1][2])
print(matriz[-1][-1])

lista1 = [1,2,3,4,5,6,7,8,9,]

print(lista1[2:]) # 3,4,5,6,7,8,9
print(lista1[:2]) # 1, 2
print(lista1[1:3]) # 2, 3
print(lista1[0:3:2]) # 1, 3
print(lista1[::]) # 1,2,3,4,5,6,7,8,9
print(lista1[::-1]) # 9, 8, 7, 6, 5, 4, 3, 2, 1

lista_2 = lista1[::-1]
print(lista_2)
print(lista1) """

# 011 Loops in listas

carros= ['gol', 'celta', 'fusca']

for index, carro in enumerate(carros):
    print(f'{index +1}: {carro}')
    
numeros = [1,30,21,2,9,65,34]

pares = [numero for numero in numeros if numero % 2 == 0]  
print(pares)  

quadrado =[]
for numero in numeros:
    quadrado.append(numero ** 2)    
print(quadrado)
    
quadrado2= [numero ** 2 for numero in numeros]
print(quadrado2)

quadrado2.clear()

print(quadrado2)

lista_3 = [1, 'palavra', [1,3,6]]

lista_4 = lista_3.copy()

print(lista_3)

print(id(lista_3), id(lista_4))

lista_4[0] = 2

print(lista_4)
print(lista_3)

lista_4.extend(['banaba', 'bonomo']) # acrescenta mais itens, append só de 1 em 1
print(lista_4)

print(lista_4.index('palavra')) # mostra a primeira exibição


lista_4.pop() # retira o ultimo item 'pilha'
print(lista_4)

lista_4.pop(1) # remove o que está np index
print(lista_4)

lista_4.remove([1,3,6]) # remove o item especificado
print(lista_4)


lista_5= ['python', 'js', 'c', 'dart']

lista_5.sort()
print(lista_5)

lista_5.sort(reverse=True)
print(lista_5)

lista_5.sort(key=lambda x: len(x)) # alinhapelo numero de caracteres
print(lista_5)

lista_5.sort(key=lambda x: len(x), reverse=True)
print(lista_5)


print(sorted(lista_5))

# CONJUNTOS
# SET # não respeita a ordem sequencial

numbers = set([1,2,3,2,2,4])

letras = set("abacaxi")

carritos = set(("palio", "gol", "celta", "palio"))

linguagens = {'python', 'java', 'java'} # conjuntos, elimina os repetidos
print(linguagens)

print(numbers)
print(carritos)
print(letras)

# Não aceita indexação
# para acessar o index precisa converter para lista..

carritos = list(carritos)
print(carritos[0]) 



# para saber o indice de um set (dicionario) usar um loop for com enumerate:
carritos = set(("palio", "gol", "celta", "kombi"))

for indice, carro in enumerate(carritos):
    print(f'{indice}: {carro}')
    
# para imprimir só os itens:
for item in carritos:
    print(item)
    
# CONJUNTOS

conjunto_a = {1,2}
conjunto_b = {3,4}

# para  unir 
print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4}

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
# intersecção
print(conjunto_a.intersection(conjunto_b)) # {2, 3}

# Diferença
print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

# Diferença simétrica
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# Para saber se é subconjunto
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a)) # False


print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True

# Se os itens se 'tocam' repetem
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b)) # Ture
print(conjunto_a.isdisjoint(conjunto_c)) # False 

# Adicionar, se já existir o elemento é ignorado
sorteio = {1,23}

sorteio.add(25)
print(sorteio) # {1, 25, 23}
sorteio.add(42)
print(sorteio) # {1, 42, 25, 23}
sorteio.add(25) # {1, 42, 25, 23}
print(sorteio)

# para apagar -> .clear()

# para copiar .copy()

# para descartar um item
sorteio.discard(1) # se existir descarta
sorteio.discard(89) # se não existir ignora o comando
print(sorteio)


# Pop elimina o primeiro item
numeros = {1,2,3,4,5,6,7,8,9,0}

numeros.pop() # 0
numeros.pop() # 1
print(numeros) # {2, 3, 4, 5, 6, 7, 8, 9}

# REMOVE, se o index não existir dá erro...

numeros = {0, 1,2,3,4,5,6,7,8,9,}

print(numeros)
numeros.remove(0) # 0
print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(len(numeros)) # 9
print(1 in numeros) # True
print(35 in numeros) # False