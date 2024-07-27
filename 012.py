# Algoritmo 012
# Entrar com uma data no formato ddmmaa e imprimir;
# dia mês e ano separados.

while True:
    data = input('Digite a data no formato ddmmaa: ').strip()
    if len(data) == 6 and data.isdigit(): # len() só funciona para strings
        data = int(data)
        # usando matemática:
        dia = data // 10000
        mes = (data % 1000) // 100
        ano = data % 100
        
        # usando slices, precisa ser uma string:
        # data = str(data)
        # dia = data[:2]
        # mes = data[2:4]
        # ano = data[-2:] # ou data[4:]
        
        print(f'Dia: {dia}', f'Mês: {mes}', f'Ano: {ano}', sep=' / ')
        break
        
    else:
        print('Valor inválido, digite novamente!')
        
        