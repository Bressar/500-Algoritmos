# Algoritmo 112
# Passagem de parametros em funções

# exemplo 1
def dizer_oi(nome):
    return f"Oi {nome}!"

def incentivar_aprender(nome):
    return f"Oi {nome} vamos aprender o Rebolation!"

def mensagem_para_creuza(funcao_mensagem):
    return funcao_mensagem("Creuza")

print(mensagem_para_creuza(dizer_oi))
print(mensagem_para_creuza(incentivar_aprender))

print('\n-----------------------------------\n' )

# exemplo 2
def mensagem(nome):
    print('executando mensagem')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá, tudo bem com você {nome}?'

def executar(funcao, nome):
    print('executando "executar"')
    return funcao(nome)

print(executar(mensagem, 'Creuzete'))
print(executar(mensagem_longa, 'Creuzete'))

print('\n-----------------------------------\n' )

