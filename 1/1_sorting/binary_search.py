# Arkadiusz Paterak - BINARY SEARCH

import random
import time

from random_list import createRandomList

# The algorithm - binary search
def binarySearch(arr, element):
    ''' Returns the index of the element in the list or raises ValueError if there is no such element. '''
    l = 0
    r = len(arr) - 1
    while l <= r:
        middle = (l + r) // 2

        if element < arr[middle]:
            r = middle - 1
        elif element > arr[middle]:
            l = middle + 1
        else:
            return middle
    
    raise ValueError

# Testing module
def testBinarySearch():
    print('Testowanie wyszukiwania binarnego . . .')
    time.sleep(1)

    element = random.randint(0, 100)

    for _ in range(1000):
        # zamieniając listę na słownik eliminuję duplikaty (które przeskadzają w porównaniu działania zaimplementowanego algorytmu z metodą .index()), potem wracam do listy
        # wyszukiwanie binarne działa na posortowanej tablicy, dlatego używam funkcji sorted()
        testing_list = sorted(list(dict.fromkeys(createRandomList()))) 

        try:
            index = binarySearch(testing_list, element)
        except ValueError:
            index = -1

        try:
            right_index = testing_list.index(element)
        except ValueError:
            right_index = -1

        if index != right_index:
            print('Algorytm wyszukiwania binarnego nie działa poprawnie.')
            return

    print('Algorytm wyszukiwania binarnego działa poprawnie.')

# The main body
def main():
    testBinarySearch()

if __name__ == '__main__':
    main()