# Algoritmo 109
# criar um organizador de eventos que divida os participantes em grupos de acordo com o tema escolhido

""" Entrada
Lista de participantes e o tema escolhido por cada um.
Saída
Dicionário agrupando os participantes por tema. """

# Dicionário para agrupar participantes por tema
eventos = {}
entradas = []

# Entrada do número de participantes
n = int(input().strip())
for _ in range(n):
    entradas.append(input().strip()) 
#print("Lista: " + lista)# For debug

for entrada in entradas:
    nome, evento = entrada.split(", ")
    if evento not in eventos:
        eventos[evento] = []
    eventos[evento].append(nome)
# print(eventos) # for debug

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
