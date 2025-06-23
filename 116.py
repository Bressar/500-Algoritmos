# Algoritmo 116
# Decoradores com Introspecção, sem isso os nomes das funções são 'trocados' durante o tempo  de execução

import functools # precisa importar functools!

def meu_decorador(funcao):
    @functools.wraps(funcao) # empacota aqui!
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
  
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá {nome}!")


print(ola_mundo.__name__)
