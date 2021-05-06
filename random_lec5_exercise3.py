import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    x = random.randrange(9, 21)
    if x % 2 == 0:
        return x
    else:
        return x + 1


print(deterministicNumber())