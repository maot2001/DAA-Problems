from gen import gen_examples
from tester import *
import wl
import axis
from ullman import perm_constructor
from time import time
import winsound


examples = gen_examples(10000)
results, times = wl.sol_examples(examples)
results2, times2 = axis.sol_examples(examples)

count1, count2 = 0, 0

for i in range(len(examples)):
    ullman_test = perm_constructor(examples[i][0],examples[i][1])

    test = are_graphs_isomorphic_matrix(examples[i][0],examples[i][1])
    
    if ullman_test != test:
        winsound.Beep(2500, 3000)
        print("\n\n\nWrong Tester\n\n\n")

    if results[i] != test or results2[i] != test:
        winsound.Beep(2500, 500)

        if results[i] != test: count1 += 1
        if results2[i] != test: count2 += 1

        print(f'Test result: {test}')
        print(f'WL result: {results[i]}')
        print(f'Axis result: {results2[i]}\n')

        print(f'\nmatrix A:\n{examples[i][0]}')
        print(f'\nmatrix B:\n{examples[i][1]}\n')

print(f'WL errors {count1/100}%')
print(f'Axis errors {count2/100}%')
winsound.Beep(2500, 1000)

