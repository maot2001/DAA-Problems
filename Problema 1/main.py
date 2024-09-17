from gen import gen_examples
from test import *
from tester import *
import networkx as nx
import matplotlib.pyplot as plt


examples = gen_examples(10)
for i in examples:
    #print(f'\nmatrix A:\n{i[0]}')
    #print(f'\nmatrix B:\n{i[1]}')
    # Crear el grafo usando la matriz de adyacencia
    G = nx.from_numpy_array(i[0])

# Dibujar el grafo
    nx.draw(G, with_labels=True)
    plt.show()
    G = nx.from_numpy_array(i[1])

# Dibujar el grafo
    nx.draw(G, with_labels=True)
    plt.show()
    are_graphs_isomorphic_matrix(i[0], i[1])
