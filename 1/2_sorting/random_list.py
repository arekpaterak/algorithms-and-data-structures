# Arkadiusz Paterak - lista z losowymi wartościami

import random

def createRandomList():
    ''' Creates a random list of integers in range from 0 to 100, which size is in range from 100 to 1000 '''
    size = random.randint(100, 1000)
    return [random.randint(0, 100) for _ in range(size)]