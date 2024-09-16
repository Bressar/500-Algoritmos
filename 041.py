# Algoritmo 41
# GRAFOS - caminho mais curto / "Dijkstra"

"""Usando frameworks do Python: 2 exemplos: NetworkX e SciPy"""

# Exemplo de como usar o algoritmo de Dijkstra com o NetworkX:
import networkx as nx

# Cria um grafo direcionado
G = nx.DiGraph()

# Adiciona as arestas com pesos
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=4)
G.add_edge('C', 'D', weight=1)

# Aplica o algoritmo de Dijkstra para encontrar o caminho mais curto de 'A' até 'D'
shortest_path = nx.dijkstra_path(G, source='A', target='D')

print("Caminho mais curto:", shortest_path)

# Também pode calcular a distância total
distance = nx.dijkstra_path_length(G, source='A', target='D')
print("Distância total:", distance)



print('--' * 40)



# Exemplo simples de uso da função dijkstra do scipy.sparse.csgraph:
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import numpy as np

# Matriz de adjacência com pesos
graph = np.array([[0, 1, 4, 0],
                  [1, 0, 2, 0],
                  [4, 2, 0, 1],
                  [0, 0, 1, 0]])

# Converte para uma matriz esparsa
graph_sparse = csr_matrix(graph)

# Aplica o algoritmo de Dijkstra (ponto de partida é o vértice 0)
dist_matrix, predecessors = dijkstra(csgraph=graph_sparse, directed=False, return_predecessors=True, indices=0)

print("Distâncias mais curtas do vértice 0 para os outros:", dist_matrix)
