# Algoritmo 99
# # transacoes_bancarias com funções

from datetime import datetime

transacoes = [0]
saldo = 0
valor = 0
agora = datetime.today()

def linha(caractere ='', numero=None):
    print(caractere * numero)

def calcular_saldo():
    while True:
        linha('--',10)
        operacao = input('''Escolha a função:
        [D] Depósito
        [R] Retirada
        [S] Saldo
        [X] Sair\n''').strip().upper()
        linha('--',10)
        
        if operacao == 'D':
            valor = float(input('Digite o valor\nR$ '))
            linha('--',10)
            if valor > 0:
                transacoes.append(valor)
            else:
                print('Número inválido!')
        
        elif operacao == 'R':
            valor = float(input('Digite o valor\nR$ '))
            linha('--',10)
            if valor > 0:
                valor = valor * -1
                transacoes.append(valor)
            else:
                print('Número inválido!')
        
        elif operacao == "S":
            linha('==', 15)
            saldo = sum(transacoes) 
            print(f'Saldo: R$ {saldo:.2f}\n{agora}')
            linha('==', 15)
        
        elif operacao == 'X':
            linha('--', 15)
            print('Encerrando o programa...')
            linha('--', 15)
            break 

        else:
            print('Operação inválida,\nTente novamente!')

calcular_saldo()


# Versão simples:

def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação e soma ao saldo
    for transacao in transacoes:
        saldo += transacao

    # Retorna o saldo formatado com duas casas decimais
    return f"Saldo: R$ {saldo:.2f}"

# Lê a entrada do usuário
entrada_usuario = input()

# Remove colchetes e espaços, depois separa os valores
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

# Converte os valores para float
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calcula o saldo
resultado = calcular_saldo(transacoes)

# Imprime o resultado
print(resultado)

# Versão extendida do código:


def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # Itera sobre cada transação
    for transacao in transacoes:
        # Verifica se o valor absoluto é maior que o limite
        if abs(transacao) > limite:
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas

# Lê a entrada
entrada = input()

# Divide a string da entrada em duas partes: lista e limite
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip())

# Converte os valores da lista de transações
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações com base no limite
resultado = filtrar_transacoes(transacoes, limite)

# Imprime no formato correto
print(f"Transações: {resultado}")

