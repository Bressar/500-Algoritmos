# Algoritmo 115
# Decoradores com passgem de argumentos nas funções ARGS e KWARGS

# exemplo 1
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar a função")
        funcao(*args, **kwargs)
        print("faz algo depois de executar a função")
        
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá {nome}!")

#ola_mundo(None)
ola_mundo("Sobervalda")


print('\n-----------------------------------\n' )


# Com retorno de valores da função decorada
# exemplo 2
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

tecnologia = aprender("Unix")
print(tecnologia)


print('\n-----------------------------------\n' )

# exemplo 3
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar a função")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar a função")
        return resultado
        
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá {nome}!")
    return nome.upper() 

resultado = ola_mundo("Marinete", 1000)
print(resultado)
