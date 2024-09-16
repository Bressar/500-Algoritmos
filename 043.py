# Algoritmo 43
# Ler um valor de hora e informar quantos minutos se passaram desde o início do dia


while True:
    try:
        hora_atual = int(input('Entre com a hora atual: '))
        if 0 < hora_atual <= 24:
            hora = hora_atual
            break
        else:
            print('Valor inválido! (dia de 24H), digite novamente!')
            print('--' * 30)
    except ValueError:
            print('Valor inválido, digite novamente!')
            print('--' * 30)

while True:
    try:
        minutos_entrada = int(input('Entre com os minutos: '))
        if 0 < minutos_entrada <= 60:
            minuto = minutos_entrada
            break
        else:
            print('Valor inválido! valor deve ser entre 1 e 60, digite novamente!')
            print('--' * 30)
    except ValueError:
            print('Valor inválido, digite novamente!')
            print('--' * 30)
        
Tempo_minuto = hora * 60 + minuto
          
print(f'Até agora se passaram {Tempo_minuto} minutos')
print('--' * 30) 
   