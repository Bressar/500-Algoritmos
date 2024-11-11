# Algoritmo 079
# Cartão de crédito - in progress

import re # para trabalhar com expressões regulares
import sqlite3

cliente = {} # trocar os dados do dicionário para um banco de dados

# Treminar oo código fazendo:

# 1 - criar um banco de dados com todas os clientes cadastrados !!

# 2-  criar interface com uma impressora da máquina windows/linux

# 3 - criar interface gráfica com Custom TKinter




print('Entre com os dados do cartão para a impressão.')
# Nome 
while True:
    try:
        nome = input('Insira o nome: ').strip().upper() # não pode haver números no nome
        if re.search(r'\d', nome):  # Verifica se há números no nome
            print('ERRO! O nome não pode conter números.')
        else:
            cliente['nome'] = nome
            break
    except Exception as e:
        print('ERRO! {e}')
# Número do cartão
while True:
    try:
        numero = input('Insira o número: ') # número de exato de 16 digitos
        if len(numero) == 16 and numero.isdigit():
            cliente['número'] = numero
            break
        else:
            print('ERRO! O número do cartão deve ter exatamente 16 dígitos.')
            print()
    except ValueError as e:
        print(f'ERRO! {e}')
# Validade do cartão
# Verificação da validade: formato MM/AA
while True:
    try:
        validade = input('Insira a validade: ').strip()
        if re.match(r'^(0[1-9]|1[0-2])/\d{2}$', validade):  # Verifica o formato MM/AA
            cliente['data_validade'] = validade
            break
        else:
            print('ERRO! A validade deve estar no formato MM/AA (exemplo: 07/27).')
    except Exception as e:
        print(f'ERRO! {e}')
# Código de verificação
while True:
    try:
        codigo_verificacao = input('Insira o código de verificação: ') # número de exato de 3 digitos
        if len(codigo_verificacao ) == 3 and codigo_verificacao .isdigit():
            cliente['CVV'] = codigo_verificacao
            break
        else:
            print('ERRO! O número do cartão deve ter exatamente 3 dígitos.')
            print()
    except ValueError as e:
        print(f'ERRO! {e}')
        


print('\nCARTÂO DE CRÉDITO')
print(f'Nome: {nome}\n'
      f'N°: {numero}\n'
      f'Válido até: {validade}\n'
      f'CVV: {codigo_verificacao}')

print(cliente) # for debug

