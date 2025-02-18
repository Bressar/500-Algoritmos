# Algoritmo 87
# 
# Cálculo de dosagem de remédio a partir da idade/peso, usando dados de uma tabela.

# adultos e adolescentes desde os 12 anos e acima de 60 kg -> 1000 mg
# abaixo de 60 kg -> 875 mg

# abaixo de 12 anos, seguir tabela peso corpóreo.

#  menos de 5 kg -> não deve tomar o remédio
# 5 a 9 kg -> 125 mg
# 9.1 a 16 kg -> 250 mg
# 16.1 a 24 kg -> 375 mg
# 24.1 a 30 kg -> 500 mg
# acima de 30 kg - > 750 mg

tabela_posologia = [
    [9, 125],   # Até 9 kg -> 125 mg
    [16, 250],  # Até 16 kg -> 250 mg
    [24, 375],  # Até 24 kg -> 375 mg (corrigido)
    [30, 500],  # Até 30 kg -> 500 mg
    [float('inf'), 750]  # Acima de 30 kg -> 750 mg
]

dosagem = 0

while True:
    try:
        idade = int(input('Idade: '))
        break
    except ValueError:
        print('Valor inválido!')

while True:        
    try:
        peso = float(input('Peso: '))
        break
    except ValueError:
        print('Valor inválido!')
       
if peso < 5:
    print('Peso insuficiente para tomar a medicação!')
    exit()

elif idade >= 12:
    if peso > 60:
        dosagem = 1000
    else:
        dosagem = 875    
else:
    for limite_peso, miligramas in tabela_posologia:
        if peso <= limite_peso:
            dosagem = miligramas
            break 
               
gotas = int(dosagem / 25) # valor aletório da concentrção do remédio por mg
    
print(f'Com a idade de {idade} anos e o peso de {peso} kgs.\nA dosagem é de {gotas} gotas')

