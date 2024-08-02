# Algoritmo 019
# Dígito da Vida

# exemplo:

# 1º de Janeiro de 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 é o dígito que procurávamos e encontramos.

# peça ao usuário sua data de nascimento
# (no formato YYYYMMDD, ou YYYYDDMM, ou MMDDYYYY – na verdade, a ordem dos dígitos não importa)
# exiba o Dígito da Vida para a data.

while True:
    try:
        nascimento = int(input('Insira sua data de nascimento no formato [YYYYMMDD]: '))
        numeros = str(nascimento)
        numeros_lista = []
        lista_inteiros = []
        soma = 0
        soma_str = ''
        soma_2 = 0
        for i in numeros:
            numeros_lista.append(i)
#         print(numeros_lista) for debug

        for i in numeros_lista:
             lista_inteiros.append(int(i))
        soma = sum(lista_inteiros)
#         print(lista_inteiros)  for debug      

        if  0 < soma < 9:
            print(f'O Dígito da Vida é {soma}')
            break
        else:
            soma_str = str(soma)
            for i in soma_str:
                soma_2 += int(i)
            print(f'O Dígito da Vida é {soma_2}')
            break
    except:
        print('Digite uma data válida!')
  
print(f'Data de nascimento: {nascimento}')
# print(digito_vida)
# print(numeros_lista)
# print(sum(lista_inteiros))

# versão pro

date = input("Insira sua data de nascimento (no formato: YYYYMMDD or YYYYDDMM, 8 digitos): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1: # quando date for maior que um caracter, pára o loop
        the_sum = 0
        for dig in date:
            the_sum += int(dig) # vai somando os números até chegar em 1 digito
        print(date)
        date = str(the_sum)
    print("Seu digito da vida é: " + date)
    
    