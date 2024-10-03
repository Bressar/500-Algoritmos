# Algoritmo 58
# Análise de Empréstimo

def analise_emprestimo(valor_salario=None, valor_prestacao=None, porcentagem_maxima=None):
    if valor_salario != None and valor_prestacao != None and porcentagem_maxima != None:
        print('--' * 20)
        if valor_prestacao <= (valor_salario * porcentagem_maxima) / 100:
            print(f'Empréstimo Concedido.')
            print('--' * 20)
            
    else:        
        print('--' * 20)
        while True:
            try:
                valor_salario = float(input("Valor do Salário: € "))
                break
            except ValueError:
                print("Valor inválido, digite novamente")
                print('--' * 20)
        while True:
            try:
                valor_prestacao = float(input("Valor da prestação: € "))
                break
            except ValueError:
                print("Valor inválido, digite novamente")
                print('--' * 20)
        while True:
            try:
                porcentagem_maxima = float(input("Taxa Máxima de Porcentagem do Salário: % "))
                break
            except ValueError:
                print("Valor inválido, digite novamente")
                print('--' * 20)               
    print('--' * 20)
    if valor_prestacao <= (valor_salario * porcentagem_maxima) / 100:
        print(f'Empréstimo Concedido.')
        print('--' * 20)
    else:
        print(f'Empréstimo negado.')
        print('--' * 20)

      
analise_emprestimo(100, 30, 20)
analise_emprestimo()
             