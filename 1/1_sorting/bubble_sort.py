# Arkadiusz Paterak - BUBBLE SORT

import time

from random_list import createRandomList

# The algorithm - bubble sort
def bubbleSort(arr):
    ''' Bubble sort with a flag 'swapped' '''
    lenght = len(arr)
    for i in range(lenght - 1):
        swapped = False
        for j in range(lenght - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1], swapped = arr[j + 1], arr[j], True
        if not swapped:
            break

# Testing module
def testBubbleSort():
    print('Testowanie sortowania bąbelkowego . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        bubbleSort(testing_list)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testBubbleSort()

if __name__ == '__main__':
    main()