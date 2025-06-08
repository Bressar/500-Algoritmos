# Algoritmo 100
# Mais estruturas de repetição (Arrays)

def desafio2():
    print("zonal\n")
    for a in range(1, 9):  # a vai de 1 até 8
        print("\t", end="")  # imprime tabulação sem quebrar a linha
    print(" zona9 ")
    print(" \n ")

desafio2()

def desafio3():
    print("\nTODOS\n")
    for linha in range(1, 10):  # L de 1 a 9
        for coluna in range(1, 10):  # c de 1 a 9
            print(f"{linha}-{coluna}\t", end="")  # imprime na mesma linha com tab
        print()  # quebra de linha após o loop interno
    print("\n")

desafio3()



def desafio4():
    print("\nACIMA DA DIAGONAL PRINCIPAL\n")
    for L in range(1, 10):  # L de 1 a 9
        for t in range(1, L):  # imprime L-1 tabulações ANTES da linha
            print("\t", end="")

        for c in range(L + 1, 11):  # c de L+1 até 10
            print(f"{L}-{c}\t", end="")  # imprime L-c com tab
        print()  # quebra de linha após linha de pares
    print("\n")

desafio4()
    
def desafio5():
    print("\nTODOS\n")
    for linha in range(0, 10):  # L de 0 a 9
        for coluna in range(0, 10):  # c de 0 a 9
            print(f"{linha}-{coluna}\t", end="")  # imprime na mesma linha com tab
        print()  # quebra de linha após o loop interno
    print("\n")

desafio5()
