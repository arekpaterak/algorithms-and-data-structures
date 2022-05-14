# Arkadiusz Paterak - INSERT SORT

import time

from random_list import createRandomList

# The algorithm - insert sort
def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        insertion = arr[i]
        j = i - 1
        while j >= 0 and insertion < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insertion

# Testing module
def testInsertSort():
    print('Testowanie sortowania przez wstawianie . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        insertSort(testing_list)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testInsertSort()

if __name__ == '__main__':
    main()