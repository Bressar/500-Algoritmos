# Algoritmo 033
# Lista encadeada - inserção de dados e Fila (Stack)
# Circulares e não circulares

lista1 = [9, 6, 5, 0]
lista2 = []

def inserir_elemento_na_lista(lista):
    while True:
        try:
            novo_elemento = int(input("Digite o novo elemento: "))
            break
        except ValueError:
            print("Valor inválido, digite novamente")
            
    print("Onde deseja inserir o elemento?")
    
    while True:
        resposta = str(input("[I]nício - [M]eio - [F]im - [E]specífico (índice) ")).strip().upper()
        
        if resposta == "I":
            lista.insert(0, novo_elemento)
            break
        elif resposta == "F":
            lista.append(novo_elemento)
            break
        elif resposta == "M":  
            if len(lista) == 0:
                lista.append(novo_elemento)
            else:
                elemento_varredura = (len(lista) // 2 ) 
                lista.insert(elemento_varredura, novo_elemento)
                break
        elif resposta == "E":
            while True:
                try:
                    index = int(input(f"Escolha a posição [0 a {len(lista)}]: "))
                    if 0 <= index <= len(lista):
                        lista.insert(index, novo_elemento)
                        break
                    else:
                            print(f"Índice fora do intervalo. Tente um valor entre 0 e {len(lista)}.")
                except ValueError:
                    print("Índice inválido, insira um número inteiro.")
            break
        else:
            print("Inválido! escolha novamente!")       
    print(lista)
    
# inserir_elemento_na_lista(lista1) # debug do código


# Pilha (Stack) FILO - first in, last out
pilha1 = []

def gerenciar_pilha(fila):
    print("O que deseja fazer ?")  
    while True:
        resposta = str(input("[A]dicionar - [R]emover - [S]air ")).strip().upper()
        if resposta == "A":
            while True:
                try:
                    numero = int(input('Digite um número: '))
                    fila.append(numero)
                    break
                except ValueError:
                    print('Valor inválido, tente novamente!') 
                                     
        elif resposta == "R":
            try:
                numero_out = int(input('Digite o número a ser removido do topo da pilha: '))
                if numero_out == fila[-1]:
                    fila.pop()
                    print(f"{numero_out} foi removido do topo da pilha com sucesso!")
                    print(f"{fila}")
                else:
                    print(f"{numero_out} não é o último item no topo da pilha!")
            except ValueError:
                print("Insira um valor válido!")
                         
        elif resposta == "S":
            print(fila)
            break
        else:
            print("Inválido! escolha novamente!")  
     
             
#gerenciar_pilha(pilha1)


# Fila - firts in, first out
fila1 = []

def gerenciar_fila(fila):
    print("O que deseja fazer ?")  
    while True:
        resposta = str(input("[A]dicionar - [R]emover - [S]air ")).strip().upper()
        if resposta == "A":
            while True:
                try:
                    numero = int(input('Digite um número: '))
                    fila.append(numero)
                    break
                except ValueError:
                    print('Valor inválido, tente novamente!') 
                                     
        elif resposta == "R":
            if len(fila) == 0:  # Verifica se a fila está vazia
                print("A fila está vazia, não há o que remover!")
            else:
                try:
                    numero_out = int(input('Digite o número a ser removido do início da fila: '))
                    if numero_out == fila[0]:
                        fila.pop(0)
                        print(f"{numero_out} foi removido do início da fila com sucesso!")
                        print(f"{fila}")
                    else:
                        print(f"{numero_out} não é o primeiro item da fila!")
                except ValueError:
                    print("Insira um valor válido!")
                         
        elif resposta == "S":
            print(fila)
            break
        else:
            print("Inválido! escolha novamente!")  
     
             
gerenciar_fila(fila1)
