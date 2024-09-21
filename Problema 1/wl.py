from time import time

def get_colors(matrix, sizes, colors):
    final = True

    if len(colors) == 0:
        for i in range(len(sizes)):
            color = sizes[i]
            if not color in colors:
                colors[color] = []
            colors[color].append(i)
            if len(colors[color]) == 2: final = False

    else:
        another_colors = {}
        for c in colors:
            for v in colors[c]:
                color = []
                
                for i in range(len(matrix[v])):
                    if matrix[v][i]:
                        color.append(str(sizes[i]))
                color = sorted(color)
                color = '_'.join(color)
                
                if not color in another_colors:
                    another_colors[color] = []
                another_colors[color].append(v)
                if len(another_colors[color]) == 2: final = False

        colors.clear()
        colors.update(another_colors)

    return final

def sol_case(case, max_iter = 2):
    G1 = case[0]
    G2 = case[1]
    sizes_G1, sizes_G2 = [], []
    colors_G1, colors_G2 = {}, {}

    for i in range(len(G1)):
        sizes_G1.append(int(sum(G1[i])))
        sizes_G2.append(int(sum(G2[i])))
    
    for i in range(max_iter):
        if get_colors(G1, sizes_G1, colors_G1) != get_colors(G2, sizes_G2, colors_G2): return False
        if len(colors_G1) != len(colors_G2): return False
        for c in colors_G1:
            try:
                if len(colors_G1[c]) != len(colors_G2[c]): return False
            except:
                return False
            
    tags_G1, tags_G2 = {}, {}
    for c in colors_G1:
        for v in colors_G1[c]:
            tags_G1[v] = c
        for v in colors_G2[c]:
            tags_G2[v] = c

    selected = []
    for i in range(len(G1)):
        i_tags_G1 = []
        for j in range(len(G1)):
            if G1[i][j]: i_tags_G1.append(tags_G1[j])
        
        i_tags_G1 = sorted(i_tags_G1)
        founded = False

        for j in range(len(G1)):
            if j in selected or tags_G1[i] != tags_G2[j]: continue
            i_tags_G2 = []
            
            for k in range(len(G1)):
                if G2[j][k]: i_tags_G2.append(tags_G2[k])

            i_tags_G2 = sorted(i_tags_G2)

            all_good = True
            for u, v in zip(i_tags_G1, i_tags_G2):
                if u != v: all_good = False

            if all_good:
                selected.append(j)
                founded = True
                break

        if not founded: return False

    return True

def sol_examples(examples):
    results, times = [], []

    for ex in examples:
        now = time()
        results.append(sol_case(ex))
        times.append(time() - now)

    return results, times