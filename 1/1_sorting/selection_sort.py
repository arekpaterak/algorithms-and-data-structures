# Arkadiusz Paterak - SELECTION SORT

import time

from random_list import createRandomList

# The algorithm - selection sort
def selectionSort(arr):
    lenght = len(arr)
    for i in range(lenght):
        min = i
        for j in range(i + 1, lenght):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

# Testing module
def testSelectionSort():
    print('Testowanie sortowania przez wybieranie . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        selectionSort(testing_list)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testSelectionSort()

if __name__ == '__main__':
    main()