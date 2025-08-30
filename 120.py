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

""" file = open("arquivos/lorem.txt", "r") # read

for linha in file.readlines(): # linha linha
    print(linha) 
    
# print(file.readlines()) #retorna todas as linhas - lista de strings

file.close()  """

print('\n---------------------------------\n')

# TIP
""" arquivo = open("arquivos/lorem.txt", "r")
while len(linha := arquivo.readline()): # enquanto houver linhas ele imprime
    print(linha)
arquivo.close """

# Resumo:
arquivo = open("arquivos/exemplo1.txt", "r")
print(arquivo.read())
arquivo.close()

print('\n---------------------------------\n')

arquivo = open("arquivos/exemplo1.txt", "r")
print(arquivo.readline())
arquivo.close()

print('\n---------------------------------\n')

arquivo = open("arquivos/exemplo1.txt", "r")
print(arquivo.readlines())
arquivo.close()

# WRITE

arquivo1 = open("arquivos/exemplo2.txt", "w") # escreve em um arquivo
arquivo1.write("Eu sou o exemplo de write!")
arquivo1.close()


arquivo2 = open("arquivos/teste1.txt", "w") # cria um arquivo novo
arquivo2.close()


""" arquivo2 = open("arquivos/teste1.txt", "w")
arquivo2.writelines("Quiprocó de Caroço")
arquivo2.close() """


arquivo2 = open("arquivos/teste1.txt", "w")
arquivo2.write("Escrevendo um novo arquivo")
arquivo2.writelines(["\nEscrevendo ", "um ", "novo ", "texto"])
arquivo2.writelines(["\nEscrevendo ", "mais ", "texto\n", "Linha 4"])
arquivo2.close()
