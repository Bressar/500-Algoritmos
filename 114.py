# Algoritmo 114
# Decoradores simples

# exemplo primeiro decorador:
def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar a função")
        funcao()
        print("faz algo depois de executar a função")
    return envelope

def ola_mundo():
    print("Olá mundo! Hard way")

# usando o decorador:
ola_mundo = meu_decorador(ola_mundo) # Jeito TOSCO -> precisa passar p/ uma variável
ola_mundo()


print('\n-----------------------------------\n' )


# exemplo decorador 'Açucarado':
def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar a função")
        funcao()
        print("faz algo depois de executar a função")
    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo! Easy way")

ola_mundo()

