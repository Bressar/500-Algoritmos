# Algoritmo 034
# Árvore Binária
# Inserir valores na árvore, buscar um valor, ou visualizar a árvore em diferentes ordens (In-Order, Pre-Order, Post-Order).

class ElementoDaArvoreBinaria:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
#  Essa classe representa um nó da árvore binária, contendo um dado e
# ponteiros para os filhos esquerdo e direito (inicialmente None).       
        

# Função para inserir um elemento na árvore binária
# Insere um número na árvore, respeitando a ordem binária (menores à esquerda, maiores à direita).
def inserir_na_arvore(raiz, numero):
    if raiz is None:
        return ElementoDaArvoreBinaria(numero)
    else:
        if numero < raiz.dado:
            raiz.esquerda = inserir_na_arvore(raiz.esquerda, numero)
        else:
            raiz.direita = inserir_na_arvore(raiz.direita, numero)
    return raiz


# Função para buscar um elemento na árvore binária
# Faz a busca recursiva de um número na árvore. Retorna o nó se o encontrar, ou None caso contrário.
def busca_na_arvore(raiz, numero):
    if raiz is None or raiz.dado == numero:
        return raiz

    if numero < raiz.dado:
        return busca_na_arvore(raiz.esquerda, numero)
    return busca_na_arvore(raiz.direita, numero)


# Função para visualizar a árvore em ordem (In-Order)
# listamos os elementos iniciando pelos elementos da esquerda;
# depois, a raiz; e, por último, os elementos da direita.
# Dessa forma, os elementos listados são apresentados ordenados
# e de forma crescente
def visualizar_arvore_ordem(raiz):
    if raiz:
        visualizar_arvore_ordem(raiz.esquerda)
        print(raiz.dado, end=" ")
        visualizar_arvore_ordem(raiz.direita)


# Função para visualizar a árvore em pré-ordem (Pre-Order)
# listamos os elementos iniciando pela raiz, depois
# listamos os elementos da esquerda, e, por fim, os elementos da direita;
def visualizar_arvore_pre_ordem(raiz):
    if raiz:
        print(raiz.dado, end=" ")
        visualizar_arvore_pre_ordem(raiz.esquerda)
        visualizar_arvore_pre_ordem(raiz.direita)


# Função para visualizar a árvore em pós-ordem (Post-Order)
# listamos os elementos iniciando pelos elementos da
# esquerda; depois, os da direita; e, por último, a raiz.
def visualizar_arvore_pos_ordem(raiz):
    if raiz:
        visualizar_arvore_pos_ordem(raiz.esquerda)
        visualizar_arvore_pos_ordem(raiz.direita)
        print(raiz.dado, end=" ")


# Função principal para interagir com o usuário
def arvore_menu():
    raiz = None
    while True:
        print("\nEscolha uma operação:")
        print("[0] Inserir na árvore")
        print("[1] Buscar na árvore")
        print("[2] Visualizar em ordem (In-Order)")
        print("[3] Visualizar em pré-ordem (Pre-Order)")
        print("[4] Visualizar em pós-ordem (Post-Order)")
        print("[5] Sair")

        op = int(input("Digite a operação desejada: "))
        if op == 5:
            break

        if op == 0:
            numero = int(input("Digite o número para inserir: "))
            raiz = inserir_na_arvore(raiz, numero)
        elif op == 1:
            numero = int(input("Digite o número para buscar: "))
            resultado = busca_na_arvore(raiz, numero)
            if resultado is not None:
                print(f"Número {numero} encontrado!")
            else:
                print(f"Número {numero} não encontrado.")
        elif op == 2:
            print("Visualização em ordem (In-Order):")
            visualizar_arvore_ordem(raiz)
            print()
        elif op == 3:
            print("Visualização em pré-ordem (Pre-Order):")
            visualizar_arvore_pre_ordem(raiz)
            print()
        elif op == 4:
            print("Visualização em pós-ordem (Post-Order):")
            visualizar_arvore_pos_ordem(raiz)
            print()
        else:
            print("Operação inválida. Tente novamente.")


# Executa o menu
arvore_menu()
