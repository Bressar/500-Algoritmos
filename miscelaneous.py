# Testes de código, comandos e funções básicas do python


# # 001
# """ texto = input('Escreva um texto:\n')

# vogais = 'AEIOU'

# for letra in texto:
#     if letra.upper() in vogais: # remove as consoantes
#         print(letra, end='')
# else:       
#     print()
#     print('Executa no final do laço') """


# # 002
# # range (stop) -> range object
# # range(start, stop[,step]) -> range object

# """ print(range(4)) # range(0, 4)

# print(list(range(4))) # [0, 1, 2, 3]  


# # 003
# """ for numero in range(0, 11):
#     print(numero, end=' ')

# print('\n')
    
# for numero in range (0, 51, 5):
#     print(numero, end= ' ') """


# 004
# opcao = -1

# while opcao != 0:
#     opcao = int(input('[1] Sacar\n[2] Extrato\n[0] Sair\n:'))
    
#     if opcao == 1:
#         print('sacando...')
#     elif opcao == 2:
#         print('Exibindo o extrato...')
# else:
#     print('Obrigado por usar o nosso sistema') """
        
        
        
 # 005
# while True:
#     numero = int(input('Informe um número: '))   
#     if numero == 10:
#         break 
    
#     if numero % 2 == 0:
#         continue
       
#     print(numero)

# print('\n')


# for numero in range(100):    
#     if numero == 10:
#         break # continue 'pula'  
#     print(numero, end =' ')
    
# print('\n')
    
# for numero in range(100):
#     if numero  % 2 == 0: # pula os pares
#         continue
#     print(numero, end =' ')

       
        
 # 006 strings
""" nome1 = "Guilherme Arthur de Carvalho"

print(nome1[0]) # G
print(nome1[:9]) # Guilherme
print(nome1[10:]) # Arthur de Carvalho
print(nome1[10:16]) # Arthur
print(nome1[10:16:2]) # Atu
print(nome1[:]) # Guilherme Arthur de Carvalho
print(nome1[::-1]) # ohlavraC ed ruhtrA emrehliuG
 
nome ='Douglas Funny'
print(nome[0])
print(nome[:9])
print(nome[:10])
print(nome[5:10])

print(nome[4:12:2])

palavra = 'text'

print(palavra.center(10, '#')) 
# ###text###

print('.'.join(palavra))
# t.e.x.t        
        



# 007 Linhas mútiplas
# menu= """
# ========== MENU =========

#  1 - Sacar
 
#  2 - Depositar
 
#  0 - Sair

# =========================

#         Obrigado por usar o nosso sistema!!

# """
# print(menu)


# 008 *Args (retorna tupla) e ** Kwargs (retorna dicionário)

def exibir_poema(data_extenso, *lista, **dicionario): # *args, **kwargs
    texto = "\n".join(lista) # vai quebrar em linhas 
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    print('\n')

#data_extenso
# Seráo primeiro parametro inserido na chamada função

# *args - lista
# Será o segundo parametro separado por vírgulas (tupla)

# **kwargs - dicionário
# Será o terceiro parametro detereminado por chave/valor (dicionário)# no caso: autor e ano


exibir_poema("Terça-Feira, 25 de Fevereiro de 2025",
             "Zen of Python", "Beautiful is better than ugly.", "Explicit is better than implicity.", "Simple is better than complex.",
             autor= "Tim Peters",
             ano=1999)



# 009 Passagem e parametros

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel): # parametros só por nome
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo='Uno', ano=1986, placa=' BU-6699', marca='Fiat', motor=1.0, combustivel='alcool')

def criar_carro1(modelo, ano, placa, /, marca, motor, combustivel): # parametros por posição e por nome
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro1('Palio', 1998,  'CE-9587', marca='Fiat', motor=1.0, combustivel='gasolina')   



# Função como um objeto (parametro)
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é: {resultado}")

exibir_resultado(10, 20, somar)
exibir_resultado(20, 10, subtrair)

# função como atribuição de uma variável
operacao = somar
print(operacao(1,23))


# Escopo GLOBAL
salario = 2000

def salario_bonus(bonus, lista):
    global salario # se não passar como argumento precisa ser uma variavel global, ou de classe self.variavel
    
    lista_copia = lista.copy() # faz uma cópia para não alterar a original
    lista_copia.append(2)
    print(f"lista cópia = {lista_copia}")
    
    salario += bonus
    return salario

lista = [1] 

salario_com_bonus = salario_bonus(500, lista) # recebe lista como parametro
print(salario_com_bonus)
print(f'Lista original: {lista}')