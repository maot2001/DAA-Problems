MIN = 100

def clean_vertex(vertex, row, i):
    new_vertex = []
    
    for v in vertex:
        if not row and f'_{i}' in v: continue
        if row and f'{i}_' in v: continue
        new_vertex.append(v)

    return new_vertex

def recursive(vertex, lines, i):
    global MIN
    if len(vertex) == 0:
        MIN = min(MIN, sum(lines))
        return
    if i == len(lines):
        return
    
    row = True if i < (len(lines) // 2) else False
    ind = i if row else i - (len(lines) // 2)

    lines[i] = 1
    recursive(clean_vertex(vertex, row, ind), lines, i+1)
    
    lines[i] = 0
    recursive(vertex, lines, i+1)


def test_case(case):
    size = len(case)
    lines = [0 for _ in range(size*2)]
    vertex = []

    for i in range(len(case)):
        for j in range(len(case)):
            if case[i][j]: vertex.append(f'{i}_{j}')

    recursive(vertex, lines, 0)

def test_examples(examples):
    global MIN
    results = []

    for ex in examples:
        test_case(ex)
        results.append(MIN)
        MIN = 100

    return results