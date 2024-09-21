from Problema_2 import Gen
from sol import sol_examples
import winsound
        
problems = Gen(1000)
sol = sol_examples(problems)

for i in range(len(problems)):
    if i % 100 == 0: print(i)
    problems[i].solve()
    if problems[i].get_max() != sol[i]:
        winsound.Beep(2500, 500)
        print(f'\n\n{i} Bad:\n{problems[i].events}\n{problems[i].time}\nresult: {problems[i].get_max()}\nbad result {sol[i]}\n\n')