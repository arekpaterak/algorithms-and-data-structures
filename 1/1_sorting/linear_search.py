# Arkadiusz Paterak - LINEAR SEARCH

import random
import time

from random_list import createRandomList

# The algorithm - linear search
def linearSearch(arr, element):
    ''' Returns the index of the first occurence of the element in the arr or raises ValueError if there is no such element. '''
    length = len(arr)
    for i in range(length):
        if arr[i] == element:
            return i
    raise ValueError

# Testing module
def testLinearSearch():
    print('Testowanie wyszukiwania liniowego . . .')
    time.sleep(1)

    element = random.randint(0, 100)

    for _ in range(1000):
        testing_list = createRandomList()

        try:
            index = linearSearch(testing_list, element)
        except ValueError:
            index = -1

        try:
            right_index = testing_list.index(element)
        except ValueError:
            right_index = -1

        if index != right_index:
            print('Algorytm wyszukiwania liniowego nie działa poprawnie.')
            return

    print('Algorytm wyszukiwania liniowego działa poprawnie.')

# The main body
def main():
    testLinearSearch()

if __name__ == "__main__":
    main()