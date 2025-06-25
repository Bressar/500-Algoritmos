# Algoritmo 117
#  Métodos Iteradores - 'iter' 'next'

# exemplo 1 - com um arquivo de texto

class Iterador_de_Arquivo:
    def __init__(self, nome_arquivo):
        self.arquivo = open(nome_arquivo)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        linha = self.arquivo.readline()
        if linha != '' :
            return linha
        else:
            self.arquivo.close()
            raise StopIteration
        
# implementação        
""" for linha in Iterador_de_Arquivo('large_file.txt'): # exemplo com arquivo de texto(gigante)
    print(linha)  """       


# exemplo 2 - com uma lista

class MeuIterador:
    def __init__(self, numeros = list[int]):
        self.numeros = numeros
        self.contador = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError: # pára a execução quando exceder o indice da lista
            raise StopIteration
        
for i in MeuIterador(numeros=[10, 30, 50]):
    print(i)