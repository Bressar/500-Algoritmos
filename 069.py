# Algoritmo 69
# Ler o nome do aluno e indicar em qual sala ele fará a prova.
# São 3 salas:
# A - K : sala 101
# L - N : sala 102
# O - Z : sala 103
# depois de concluido, gravar essas listas em um banco de dados


sala_101 = []
sala_102 = []
sala_103 = []

while True:
    # Entrada do nome e validação
    while True:
        try:
            print('--' * 30)
            nome_estudante = input("Digite o nome do(a) estudante: ").strip().title()
            if not all(part.isalpha() for part in nome_estudante.split()):
                raise ValueError("O nome deve conter apenas letras.")
            else:
                break
        except ValueError:
            print("Valor inválido! tente novamente!")

    # Determinação da sala
    primeira_letra = nome_estudante[0]
    if 'A' <= primeira_letra < 'L':
        sala_101.append(nome_estudante)
        nome_sala = 101
    elif 'L' <= primeira_letra < 'O':
        sala_102.append(nome_estudante)
        nome_sala = 102
    else:
        sala_103.append(nome_estudante)
        nome_sala = 103
        
    print(f'O aluno(a) {nome_estudante} fará a prova na sala {nome_sala}') # for debug
    print('--' * 30)
    sair = input('Para continuar pressione [C] ou [S] para sair: \n').upper()
    if sair == "S":
        print("Encerrando programa...")
        print('--' * 30)
        break


# função exibir listas
def imprimir_lista_sala(nome_sala=" ", nome_lista=[]):
    print('--' * 20)
    print("Lista de alunos na", nome_sala)
    for aluno in sorted(nome_lista):
        print(aluno, end = "\n")

    
imprimir_lista_sala("sala 101", sala_101)
imprimir_lista_sala("sala 102", sala_102)
imprimir_lista_sala("sala 103", sala_103)

