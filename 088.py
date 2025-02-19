# Algoritmo 88
# 
# De acordo com a % apresentar uma notificação, usando dados de uma tabela.

taxa_poluicao =[
    [0.3, '1°'],
    [0.4, '1° e 2°'],
    [float('inf'), '1°, 2° e 3°'] # 0.5
]
while True:
    try:
        indice = float(input('Digite o índice de poluição:\n'))
        break
    except ValueError:
        print('Valor inválido, digite novamente.')

if indice < 0.3:
    print('Índice de poluição aceitável para todos os grupos.')
    exit()
else:
    for index, grupo in taxa_poluicao:
        if indice <= index:
            resposta = grupo
            break         
print(f'Suspender as atividades das indústrias do(s) {resposta} grupo(s)')

