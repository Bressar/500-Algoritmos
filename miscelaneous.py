# Testes de código, comandos e funções básicas do python




# 005
while True:
    numero = int(input('Informe um número: '))   
    if numero == 10:
        break 
    
    if numero % 2 == 0:
        continue
       
    print(numero)

print('\n')


for numero in range(100):    
    if numero == 10:
        break # continue 'pula'  
    print(numero, end =' ')
    
print('\n')
    
for numero in range(100):
    if numero  % 2 == 0: # pula os pares
        continue
    print(numero, end =' ')



# 004
""" opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar\n[2] Extrato\n[0] Sair\n:'))
    
    if opcao == 1:
        print('sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
else:
    print('Obrigado por usar o nosso sistema') """
        

# 003
""" for numero in range(0, 11):
    print(numero, end=' ')

print('\n')
    
for numero in range (0, 51, 5):
    print(numero, end= ' ') """


# 002
# range (stop) -> range object
# range(start, stop[,step]) -> range object

""" print(range(4)) # range(0, 4)

print(list(range(4))) # [0, 1, 2, 3]  

 """

# 001
""" texto = input('Escreva um texto:\n')

vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais: # remove as consoantes
        print(letra, end='')
else:       
    print()
    print('Executa no final do laço') """