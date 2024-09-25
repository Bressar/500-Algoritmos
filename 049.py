# Algoritmo 49
# Número sucessor, !Sem usar estruturas de repetição!

""" algoritmo que lê um número entre 0 e 60 e imprime o seu sucessor, sabendo que o sucessor de 60 é 0.
Obs: Não pode ser usar nenhum comando de seleção e nem de repetição """

def numero_sucessor():
    while True:
        try:
            numero = int(input("Digite um número inteiro entre 0 e 60: "))
            if numero >= 0 and numero <= 60:
                break
            else:
                print("ERRO! Valor inválido!")
                print('--' * 25)
        except ValueError:
            print('ERRO! Valor inválido!')
            print('--' * 25)
            
    print("O número sucessor é: ", (numero + 1) % 61)
    print('--' * 25)
    
numero_sucessor()
