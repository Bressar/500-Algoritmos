# Algoritmo 91

# Verificar se uma data é válida -> dia/mês/ano - 13/8/2021

def eh_bissexto(ano):
    """Verifica se um ano é bissexto."""
    ano = int(ano)
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def obter_ano():
    """Solicita e valida o ano (deve ter 4 dígitos e ser um número)."""
    while True:
        ano = input('Ano: ').strip()
        if len(ano) == 4 and ano.isdigit():
            return int(ano)
        print('ERRO! Ano inválido!')


def obter_mes():
    """Solicita e valida o mês (deve estar entre 1 e 12)."""
    while True:
        mes = input('Mês: ').strip()
        if mes.isdigit() and 1 <= int(mes) <= 12:
            return int(mes)
        print('ERRO! Mês inválido!')


def obter_dia(mes, ano):
    """Solicita e valida o dia de acordo com o mês e ano fornecidos."""
    # Dicionário com os dias máximos de cada mês
    dias_por_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Ajusta Fevereiro se o ano for bissexto
    if mes == 2 and eh_bissexto(ano):
        dias_por_mes[2] = 29

    while True:
        try:
            dia = int(input('Dia: '))
            if 1 <= dia <= dias_por_mes[mes]:
                return dia
            print('Número de dias inválido para este mês!')
        except ValueError:
            print('ERRO! Dia inválido!')


#Executa a verificação
print('Informe a data')
ano = obter_ano()
mes = obter_mes()
dia = obter_dia(mes, ano)

# Exibe a data válida
print('--' * 20)
print(f'Data válida: {dia}/{mes}/{ano}')
print('--' * 20)









# Versão com a lógica bruta... 
print('Informe a data')
while True:
        ano = input('Ano: ').strip()
        if len(ano) == 4 and ano.isdigit():
            break
        else:
            print('ERRO! Ano inválido!')  
                
while True:  
        mes = input('Mês: ').strip()
        if len(mes) < 3 and mes.isdigit():
            mes_int = int(mes)
            if mes_int > 0 and mes_int < 13: 
                 break
            else:
                print('Mês deve ser entre 1 e 12!')
        else:
            print('ERRO! Mês inválido!')  

while True:
    try:
        dia = int(input('Dia: ')) 
              
        if dia < 0 or dia > 31:
            print('Número de dias inválido!')

        elif dia > 28 and (mes_int == 2): # * 28 ou 29
            print('Número de dias inválido!')
                
        elif dia > 30 and (mes_int == 4 or mes_int== 6 or mes_int == 9 or mes_int == 11):
            print('Número de dias inválido!') 
        
        else:
            print('--' * 20)    
            print(f'Data: {dia}/{mes_int}/{ano}')
            print('--' * 20) 
            break
        
    except ValueError:
        print('ERRO! Dia inválido')



