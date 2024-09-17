import numpy as np
import itertools

def are_graphs_isomorphic_matrix(adj_matrix1, adj_matrix2):
    """
    Checks if two graphs, represented as adjacency matrices, are isomorphic.

    Args:
        adj_matrix1: The adjacency matrix of the first graph (NumPy array).
        adj_matrix2: The adjacency matrix of the second graph (NumPy array).

    Returns:
        True if the graphs are isomorphic, False otherwise.
    """

    n = len(adj_matrix1)
    if n != len(adj_matrix2):
        return False  # Different number of nodes

    nodes = range(n)  # Nodes are represented by indices 0 to n-1

    for permutation in itertools.permutations(nodes):
        is_isomorphic = True
        for i in range(n):
            for j in range(n):
                # Check if edge (i, j) in graph1 corresponds to edge 
                # (permutation[i], permutation[j]) in graph2
                if adj_matrix1[i][j] != adj_matrix2[permutation[i]][permutation[j]]:
                    is_isomorphic = False
                    break  # This permutation doesn't work
            if not is_isomorphic:
                break  # Move to the next permutation

        if is_isomorphic:
            return True  # Found a valid isomorphism

    return False  # No permutation resulted in an isomorphism

G1 = np.array([[0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0]])

G2 = np.array([[0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0]])


# Comparar G1 y G2: True
print(are_graphs_isomorphic_matrix(G1, G2))

G3 = np.array([[0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0]])

G4 = np.array([[0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0]])

# Comparar G3 y G4: False
print(are_graphs_isomorphic_matrix(G3, G4))


