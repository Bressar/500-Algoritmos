# Algoritmo 106

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:


# TODO: Exiba a ordem de atendimento com título e vírgulas: