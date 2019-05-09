import random

def rand7():
    seed = random.randint(1,5) * 5 + random.randint(1,5) -5
    if seed < 22:
        return seed % 7 + 1
    return rand7()


print(rand7())