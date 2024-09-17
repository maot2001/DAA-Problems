from random import randint, shuffle, choice
from numpy import zeros

def gen_axis(nodes, M):
    axis = [[] for _ in range(len(nodes))]
    full = nodes.copy()
    shuffle(full)

    for i in range(1, len(full)):
        axis[full[i]-1].append(full[i-1])
        axis[full[i-1]-1].append(full[i])

    for i in range(len(axis)):
        if len(axis[i]) == (len(nodes) - 1): full.remove(i+1)

    for i in range(M - len(axis) + 1):
        ind = choice(full)
        possible = [n for n in nodes if n not in axis[ind-1] and n != ind]
        ind2 = choice(possible)
        axis[ind-1].append(ind2)
        axis[ind2-1].append(ind)
        if len(axis[ind2-1]) == (len(nodes) - 1): full.remove(ind2)
        if len(possible) == 1: full.remove(ind)

    return axis

def gen_case(N, M):
    nodes = [i for i in range(1, N+1)]
    axis = gen_axis(nodes, M)
    
    matrix = zeros((N, N))
    for i in range(N):
        for j in range(len(axis[i])):
            matrix[i][axis[i][j] - 1] = 1

    return matrix

def gen_examples(number):
    examples = []
    
    for _ in range(number):
        N = randint(2, 10)
        M = randint(N - 1, (N * (N-1) // 2))
        matrix = gen_case(N, M)
        new_matrix = gen_case(N, M)
        examples.append((matrix, new_matrix))
    
    return examples