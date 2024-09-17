import numpy as np
from itertools import permutations

def perm_constructor(G1, G2):
    Permutation_list = []
    n1 = len(G1)
    n2 = len(G2)
    for perm in permutations(range(n1),n2):
        not_valid_perm = False
        p = np.array([np.zeros(n1) for _ in range(n2)])
        
        for i in range(len(perm)):
            if sum(G1[perm[i]]) != sum(G2[i]):
                not_valid_perm = True
                break
        if not_valid_perm:
            continue
        for k in range(n2):
            p[k][perm[k]]=1
        Permutation_list.append(p)
    return Permutation_list

def isomorph(G1,G2,permut):
    for P in permut:
        if np.array_equal(P @ G1 @ P.T, G2):
            return True
    return False

