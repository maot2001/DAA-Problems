from random import randint

def gen_case(size, k):
    square = [[False for _ in range(size)] for _ in range(size)]

    for _ in range(k):
        up = randint(0, size - 1)
        left = randint(0, size - 1)
        down = randint(up, size - 1)
        right = randint(left, size - 1)
        for i in range(up, down + 1):
            for j in range(left, right + 1):
                square[i][j] = True

    return square

def gen_examples(number):
    examples = []
    
    for _ in range(number):
        size = randint(2, 10)
        k = randint(1, 6)
        square = gen_case(size, k)
        examples.append(square)
    
    return examples