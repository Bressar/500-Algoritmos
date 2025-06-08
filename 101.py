# Algoritmo 100
# Mais estruturas de repetição

def desafio2():
    print("zonal\n")
    for a in range(1, 9):  # a vai de 1 até 8
        print("\t", end="")  # imprime tabulação sem quebrar a linha
    print(" zona9 ")
    print(" \n ")

#desafio2()

def desafio3():
    print("\nTODOS\n")
    for linha in range(1, 10):  # L de 1 a 9
        for coluna in range(1, 10):  # c de 1 a 9
            print(f"{linha}-{coluna}\t", end="")  # imprime na mesma linha com tab
        print()  # quebra de linha após o loop interno
    print("\n")

desafio3()

    