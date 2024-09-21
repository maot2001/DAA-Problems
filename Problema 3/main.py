from gen import gen_examples
from tester import test_examples
from sol import sol_examples

problems = gen_examples(100)
test = test_examples(problems)
results = sol_examples(problems)

for i in range(len(problems)):
    if test[i] == results[i]: continue
    for row in problems[i]:
        text = '[ '
        for e in row:
            if e: text += 'X '
            else: text += 'O '
        text += ']'
        print(text)
    print(f'test: {test[i]}')
    print(f'result: {results[i]}')
    print()

print('DONE!!!')