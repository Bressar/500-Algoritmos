# Algoritmo 106
# Ordenar lista de pacientes por idade e prioridade
""" 
 Critérios de Prioridade: Pacientes acima de 60 anos têm prioridade. Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima. Os demais pacientes são atendidos por ordem de chegada. Entrada Um número inteiro n, representando a quantidade de pacientes. n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status nome: string representando o nome do paciente. idade: número inteiro representando a idade do paciente. status: string que pode ser "urgente" ou "normal". Saída A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3 """

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for i in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status, i)) # i representa a ordem de chegada

# TODO: Ordene por prioridade: urgente > idosos > demais:

def prioridade(paciente):
    nome, idade, status, ordem_chegada = paciente
    
    if status == "urgente":
        return (0, -idade, ordem_chegada)  # Urgentes: por idade decrescente, depois ordem chegada
    elif idade >= 60 and status == "normal":
        return (1, -idade, ordem_chegada)  # Idosos normais: por idade decrescente, depois ordem chegada
    else:
        return (2, ordem_chegada)  # Demais: apenas ordem de chegada  

# TODO: Exiba a ordem de atendimento com título e vírgulas:
# Ordene por prioridade: urgente > idosos > demais
pacientes_ordenados = sorted(pacientes, key=prioridade)

# Extrair apenas os nomes para a saída
nomes_ordenados = [paciente[0] for paciente in pacientes_ordenados]

# Exiba a ordem de atendimento com título e vírgulas
print("Ordem de Atendimento: " + ", ".join(nomes_ordenados))

