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


lista_5= ['pytho', 'js', 'c', 'dart']

lista_5.sort()
print(lista_5)