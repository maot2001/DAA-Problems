import numpy as np
from itertools import permutations

def neighbor_degrees(G, v):
    return sorted(np.sum(G, axis=1)[G[v] == 1])

def perm_constructor(G1, G2):
    n1 = len(G1)
    if sorted(np.sum(G1,axis=1)) != sorted(np.sum(G2, axis=1)):
        return False
    if sorted([neighbor_degrees(G1, i) for i in range(n1)]) != sorted([neighbor_degrees(G2, j) for j in range(n1)]):
        return False
    
    for perm in permutations(range(n1)):
        p = np.eye(n1)[list(perm)]
        if np.array_equal(p @ G1 @ p.T, G2):
            return True
    return False