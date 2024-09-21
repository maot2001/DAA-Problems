from random import randint, choice
from numpy import zeros

def dfs(graph, node, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def connected_components(graph):
    visited = set()
    components = []

    for i in range(len(graph)):
        if i not in visited:
            component = []
            dfs(graph, i, visited, component)
            components.append(component)

    return components

def gen_axis(nodes, M):
    axis = [[] for _ in range(len(nodes))]
    full = nodes.copy()

    for _ in range(M):
        ind = choice(full)
        possible = [n for n in nodes if n not in axis[ind] and n != ind]
        ind2 = choice(possible)
        axis[ind].append(ind2)
        axis[ind2].append(ind)
        if len(axis[ind2]) == (len(nodes) - 1): full.remove(ind2)
        if len(possible) == 1: full.remove(ind)

    return axis

def merge_components(axis, components):
    sizes_c = []

    for c in components:
        size = 0
        for v in c: size += len(axis[v])
        sizes_c.append((size // 2) - (len(c) - 1))

    iterations = len(components) - 1

    for _ in range(iterations):
        possible = [i for i in range(len(sizes_c)) if sizes_c[i] > 0]
        comp_A = components[choice(possible)]
        
        possible = [c for c in components if c != comp_A]
        comp_B = choice(possible)

        deleted = [x for x in comp_A if len(axis[x]) > 1]

        if len(deleted) != len(comp_A):
            for x in comp_A:
                if x in deleted and len(set(deleted) & set(axis[x])) == 0:
                    deleted.remove(x)

        u = choice(deleted)
        deleted.remove(u)

        v = choice(deleted)
        deleted.remove(v)

        while len(axis[u]) < 2 or len(axis[v]) < 2 or not v in axis[u]:
            modified = False
            if len(axis[u]) < 2:
                u = choice(deleted)
                deleted.remove(u)
                modified = True

            if len(axis[v]) < 2:
                v = choice(deleted)
                deleted.remove(v)
                modified = True

            if not modified and not v in axis[u]:
                v = choice(deleted)
                deleted.remove(v)

        axis[u].remove(v)
        axis[v].remove(u)

        u = choice(comp_A)
        v = choice(comp_B)

        axis[u].append(v)
        axis[v].append(u)


def gen_case(N, M):
    nodes = [i for i in range(N)]
    axis = gen_axis(nodes, M)
    components = connected_components(axis)

    if len(components) > 1: merge_components(axis, components)
    
    matrix = zeros((N, N))
    for i in range(N):
        for j in range(len(axis[i])):
            matrix[i][axis[i][j]] = 1

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