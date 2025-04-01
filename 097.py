# Algoritmo 97
# DateTime

# python -m venv nome_do_ambiente
# nome_do_ambiente\Scripts\Activate


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

""" print(data_atual.strftime("%d/%m/%Y %H:%M")) """

data_hora_atual = datetime.now()
data_hora_str = '2025-03-20 18:50'
mascara_ptbr = "%d/%m/%Y %H:%M"

mascara_en = "%Y-%m-%d %H:%M"  # Corrigido os separadores

print(data_hora_atual.strftime(mascara_ptbr))  # Corrigido o nome da variável

data_convertida  = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

print('---' * 30)

# Timezone com pytz (melhor maneira)
import pytz
from datetime import datetime, timezone, timedelta

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))
data3 = datetime.now(pytz.timezone('Europe/Lisbon'))

print(f'Oslo: {data}\nSão Paulo: {data2}\nLisboa: {data3}')


print('---' * 30)
# Timezone usando só o datetime

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSL")) # valor do nome é opcional +2
data_sp = datetime.now(timezone(timedelta(hours=-3))) # -3

print(f'Oslo: {data_oslo}\nSão Paulo: {data_sp}')

# convertendo para outro timezone
""" d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)
 """