# Algoritmo 102
# Mais estruturas de repetição (Listas)

from math import sqrt

def lista1():
    for i in range(1, 101): # de 1 a 100
        print(i, end=" ")
    print("\n")
    
#lista1()

def lista2():
    for i in range(100, 0, -1):  # começa em 100, termina em 1 (inclusive), passo -1
        print(i, end=" ")
    print("\n")

#lista2()

def lista3():
    for i in range(2, 201, 2): # de 2 a 200, 100 primeiros pares
        print(i, end=" ")
    print("\n")
    
#lista3()

def lista4():
    for i in range(5, 501, 5): # 100 primeiros multiplos de 5
        print(i, end=" ")
    print("\n")
    
#lista4()

def lista5():
    for i in range(1, 21): # quadrados de 1 até 20
        print(i**2, end=" ")
    print("\n")
    
#lista5()

def lista6():
    for i in range(120, 301):#intervalo entre 120 e 300
        print(i, end=" ")
    print("\n")
    
#lista6()


def lista7():
    soma= 0
    for i in range(1, 101):#somatorio de 1 a 100
        print(i, end=" ")
        soma += i
    print(f"\nSomatória de 1 a 100: {soma}\n")
    
#lista7()

def lista8(): # Entrar com 10 números e imprimir a metade de cada número.
    for i in range(1, 11):
        numero= float(input("Digite número: "))
        print(f"Metade: {numero / 2}")
    print("\n")
    
#lista8()

def lista9(): # Entrar com 5 números e imprimir a raiz quadrada de cada número.
    for i in range(1, 6):
        numero= float(input("Digite número: "))
        raiz = sqrt(numero)
        print(f"Raiz: {raiz}")
    print("\n")
    
lista9()

