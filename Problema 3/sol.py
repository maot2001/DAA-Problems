from edmonds_karp import Graph

def sol_case(case):
    size = len(case)
    graph = [[0 for _ in range(2*size+2)] for _ in range(2*size+2)]

    for i in range(size):
        graph[2*size][i] = 1
        graph[size+i][2*size+1] = 1
        for j in range(size):
            if case[i][j]:
                graph[i][size+j] = 1

    graph = Graph(graph)
    return graph.EdmondsKarp(2*size, 2*size+1)


def sol_examples(examples):
    results = []

    for ex in examples:
        results.append(sol_case(ex))

    return results