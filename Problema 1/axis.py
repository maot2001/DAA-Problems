from time import time

def sol_case(case):
    G1 = case[0]
    G2 = case[1]
    sizes_G1, sizes_G2 = [], []
    axis_G1, axis_G2 = [], []

    for i in range(len(G1)):
        sizes_G1.append(int(sum(G1[i])))
        sizes_G2.append(int(sum(G2[i])))

    for i in range(len(G1)):
        for j in range(i+1, len(G1)):
            if G1[i][j]:
                MIN = min(sizes_G1[i], sizes_G1[j])
                MAX = max(sizes_G1[i], sizes_G1[j])
                axis_G1.append((MIN, MAX))
            if G2[i][j]:
                MIN = min(sizes_G2[i], sizes_G2[j])
                MAX = max(sizes_G2[i], sizes_G2[j])
                axis_G2.append((MIN, MAX))

    axis_G1 = sorted(axis_G1)
    axis_G2 = sorted(axis_G2)

    for i in range(len(axis_G1)):
        if axis_G1[i] != axis_G2[i]: return False
    
    return True

def sol_examples(examples):
    results, times = [], []

    for ex in examples:
        now = time()
        results.append(sol_case(ex))
        times.append(time() - now)

    return results, times