# Algoritmo 107
# Sistema de reservas em uma pousada

""" Descrição
Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba uma lista de quartos disponíveis e uma lista de reservas solicitadas. A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas por falta de disponibilidade.

Entrada
Uma lista contendo os números dos quartos disponíveis.
Uma lista contendo os números dos quartos solicitados pelos clientes.
Saída
Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas. """

def processar_reservas():
    # Entrada dos quartos disponíveis
    # cria uma variável quartos_disponiveis que armazena quartos disponíveis como inteiros únicos
    #quartos_disponiveis = set(map(int, input().split()))
    
    quartos_disponiveis = set(map(int, input("Digite os quartos disponíveis: ").split()))
    #print(quartos_disponiveis) # for DEBUG
    # map(int, ... ->  Aplica a função int() a cada item da lista.
    #Converte o resultado de map() em um set (conjunto), eliminando duplicatas automaticamente se houver
     # input().split() → ['101', '102', '103'] # .split() separa a linha em partes, usando espaços como separador por padrão.
    
    # Entrada das reservas solicitadas
    # Recebe uma linha de entrada do usuário, separa os valores digitados (por espaço),
    # converte cada um para inteiro e guarda tudo em uma lista de inteiros chamada
    reservas_solicitadas = list(map(int, input("Digite as reservas solicitadas: ").split())) # lista
    """     Passo a passo:
        input()
        Lê uma linha digitada pelo usuário, por exemplo: "2 5 8 10"
        .split()
        Divide a string em pedaços separados por espaços, formando uma lista de strings:
        ['2', '5', '8', '10']
        map(int, ...)
        Aplica a função int() a cada elemento da lista para transformar as strings em números inteiros. O resultado é um iterador com os valores [2, 5, 8, 10].
        list(...)
        Converte o iterador retornado por map em uma lista concreta de inteiros: [2, 5, 8, 10]
    """
   
    # TODO: Crie o processamento das reservas:
    confirmadas = []
    recusadas = []
    
    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos:
    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            confirmadas.append(quarto) # leva para a lista de confirmadas
            quartos_disponiveis.remove(quarto)  # Remove da disponibilidade após confirmação
        else:
            recusadas.append(quarto) # leva para a lista de recusadas
    

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()

