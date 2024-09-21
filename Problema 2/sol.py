from numpy import zeros

def score(type, fb):
    if type == 1 and fb > 2:
        return 1
    
    if type == 2 and fb < 2:
        return 1

    return 0

def sol_case(case):
    M = [int(v) for v in list(case.events.keys())]
    T = [case.events[m] for m in case.events]
    N = max(M) + 1

    event, index = M[0], 0
    dp = zeros((N, 5))
    possibles = [2]

    for i in range(N-1):
        next_iter = []
        for j in possibles:

            if i+1 == event:
                if j-1 > -1:
                    s = score(T[index], j-1)
                    if s and not j-1 in next_iter: next_iter.append(j-1)
                    if s:
                        dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j] + 1)
                    else:
                        if not 2 in next_iter: next_iter.append(2)
                        dp[i+1][2] = max(dp[i+1][2], dp[i][j])

                if j+1 < 5:
                    s = score(T[index], j+1)
                    if s and not j+1 in next_iter: next_iter.append(j+1)
                    if s:
                        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                    else:
                        if not 2 in next_iter: next_iter.append(2)
                        dp[i+1][2] = max(dp[i+1][2], dp[i][j])

            else:
                if j-1 > -1:
                    if not j-1 in next_iter: next_iter.append(j-1)
                    dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j])

                if j+1 < 5:
                    if not j+1 in next_iter: next_iter.append(j+1)
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

        if i+1 == event:
            index += 1
            if index != len(M): event = M[index]

        possibles = next_iter.copy()

    return int(max(dp[-1]))

def sol_examples(examples):
    result = []

    for ex in examples:
        result.append(sol_case(ex))

    return result