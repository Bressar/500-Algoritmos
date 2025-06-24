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
    