# Algoritmo 99
# # transacoes_bancarias
''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''
def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    
        # TODO: Adicione o valor da transação ao saldo
        

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
  
transacoes = [0]
saldo = 0
valor= 0

while True:
    operacao = input('''Escolha a função:
    [D] Depósito
    [R] Retirada
    [S] Saldo\n''').strip().upper()
    
    if operacao == "S":
      print(f'Saldo: {saldo:.2f} €')
      break
  
    elif operacao == 'D':
        valor = float(input('Digite o valor\n'))
        transacoes.append(valor)
       #print(transacoes)
        break
    
    elif operacao == 'R':
        valor = float(input('Digite o valor\n'))
        valor = valor * -1
        transacoes.append(valor)
       #print(transacoes)
        break

    else:
        print('Operação inválida, tente novamente!')

print(operacao)

saldo = sum(transacoes)   
print(f'Saldo: {saldo:.2f} €')  
#rint(transacoes)

""" entrada_usuario = float(input('Digite '))

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado) """




""" def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    
        # TODO: Adicione o valor da transação ao saldo
        

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado) """