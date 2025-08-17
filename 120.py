# Algoritmo 120
# Manipulação de arquivos em Python (eu sei que não é algoritmo...)


# exemplos

""" file = open("arquivos/exemplo1.txt", "r") # read
file.close() 

file = open("arquivos/exemplo1.txt", "w") # write
file.close() 

file = open("arquivos/exemplo1.txt", "a") # append
file.close() 
 """
 
 # READ
""" file = open("arquivos/exemplo1.txt", "r") # read
print(file.read()) # imprime todo o arquivo
file.close()  """
 
 
file = open("arquivos/lorem.txt", "r") # read
print(file.read()) # imprime todo o arquivo
file.close() 

print('\n---------------------------------\n')

file = open("arquivos/lorem.txt", "r") # read

for linha in file.readline(): # linha linha
    print(linha) 
    
# print(file.readlines()) #retorna todas as linhas - lista de strings

file.close() 

print('\n---------------------------------\n')

# TIP
""" arquivo = open("arquivos/lorem.txt", "r")
while len(linha := arquivo.readline()): # enquanto houver linhas ele imprime
    print(linha)
arquivo.close """

# Resumo:
arquivo = open("arquivos/exemplo1", "r")
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())
arquivo.close()

print('\n---------------------------------\n')