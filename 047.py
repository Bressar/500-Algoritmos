# Algoritmo 47
# Entrar com um número real e imprimir: 
# parte inteira, parte fracionário, número arredondado

# Easy way - usando funções básicas do Python round e int -'fazendo casting'

def decompondo_numero():
    while True:
        try:
            numero = float(input("Entre com um número com parte fracionária: "))
            break
        except ValueError:
            print("ERRO! valor inválido!")

    parte_inteira = int(numero)
    parte_fracionaria = numero - parte_inteira
    numero_arredondado = round(numero)

    print('--' * 20)
    print(f'Parte inteira: {parte_inteira}')
    print(f'Parte fracionária: {parte_fracionaria}')
    print(f'Número arredondado: {numero_arredondado}')
    print('--' * 20)


decompondo_numero()



# Sem usar funções, cálculos feitos manualmente
while True:
    try:
        numero = float(input("Entre com um número com parte fracionária: "))
        break
    except ValueError:
        print("ERRO! valor inválido!")

# Parte inteira
if numero >=0:
    parte_inteira = numero // 1 # Para números positivos, usa divisão inteira
else:
    parte_inteira = (numero // 1) + 1  # Para números negativos, ajusta a parte inteira

#Parte fracionária
parte_fracionaria = numero - parte_inteira

#Número arredondado
if parte_fracionaria >= 0.5:
    numero_arredondado = parte_inteira + 1
else:
    numero_arredondado = parte_inteira

print(f'Parte inteira: {int(parte_inteira)}')
print(f'Parte fracionária: {parte_fracionaria}')
print(f'Número arredondado: {int(numero_arredondado)}')


""" 
OBSERVAÇÃO IMPORTANTE:

EXEMPLO de número negativo e arredondamento.

Supondo que o número de entrada seja:
    -89.6574645

Na primeira execução (com int() e round()):
A função int() trunca a parte fracionária, retornando -89, e a função round() arredonda o número para -90.

Na segunda execução (cálculo manual):
A divisão inteira // arredonda para -90 (parte inteira), mas o arredondamento final retorna -89, porque a parte fracionária é menor que 0.5.

Conclusão:
A abordagem mais correta para a maioria das situações seria a que segue o arredondamento simétrico (round() do Python), pois ela mantém a consistência ao lidar com números negativos e positivos de maneira uniforme.  """

