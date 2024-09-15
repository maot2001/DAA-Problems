from gen import gen_examples
from tester import test_examples

problems = gen_examples(10)
test = test_examples(problems)

for i in range(len(problems)):
    for row in problems[i]:
        text = '[ '
        for e in row:
            if e: text += 'X '
            else: text += 'O '
        text += ']'
        print(text)
    print(f'result: {test[i]}')
    print()