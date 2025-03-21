# Algoritmo 97
# Date e Time

from datetime import date, datetime, time, timedelta


# Básico

data = date(2025, 3, 20) # data aleatória
hoje = date.today() # data de hoje

data_e_hora = datetime(2025, 3, 20, 19, 35, 50) # data aleatória com horas, minutos, segundos
agora = datetime.today()

horas = time(19, 40, 0) # horário aleatório

print(f'{data}\n')
print(f'{hoje}\n')
print(f'{data_e_hora}\n')
print(f'{agora}\n')
print(f'{horas}\n')

d = datetime(2025, 3, 20, 19, 45)
print(f'{d}\n')

# adicionando uma semana
d = d + timedelta(weeks=1)
print(f'{d}\n')



print('---' * 30)
# Exemplo com carro (lava-rápido)

tipo_carro = 'P' # P, M , G
tempo_pequeno = 30 # em minutos
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # ou today() ou utcnow() -> não guarda o fuso

while True:
    tipo_carro = input('Informe o tipo do carro:\n[P] pequeno - [M] médio - [G] grande\n').upper().strip()

    if tipo_carro == 'P':
        data_estimada = data_atual + timedelta(minutes=tempo_pequeno) # days, months, years e etc.
        break
    elif tipo_carro == 'M':
        data_estimada= data_atual + timedelta(minutes=tempo_medio)
        break
    elif tipo_carro == 'G':
        data_estimada = data_atual + timedelta(minutes=tempo_grande)
        break
    else:
        print('Escolha inválida, tente novamente!')

print(f'O carro chegou: {data_atual}\ne ficará pronto às: {data_estimada}')
print('---' * 30)


print(date.today() - timedelta(days=1)) # subtrai 1 dia

resultado = datetime(2025, 3, 20, 20, 15, 0) - timedelta(hours=1) # subtrai só uma hora
print(resultado.time())

print(datetime.now().date())

print('---' * 30)

# Formatando datas e horários

