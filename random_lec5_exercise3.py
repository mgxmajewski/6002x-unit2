import random


def deterministic_number():
    """
    Deterministically generates and returns an even number between 9 and 21
    """
    random.seed(0)
    x = random.randrange(9, 21)
    if x % 2 == 0:
        return x
    else:
        return x + 1


def stochastic_number():
    """
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    """
    # Your code here
    random.seed()
    x = random.randrange(9, 21)
    if x % 2 == 0:
        return x
    else:
        return x + 1


print('deterministic: ' + str(deterministic_number()))
print('deterministic: ' + str(stochastic_number()))


