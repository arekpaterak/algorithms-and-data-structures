# Arkadiusz Paterak - COUNTING SORT

import time

from random_list import createRandomList

# The algorithm
def countingSort(arr, k):
    length = len(arr)
    count = [0] * k
    output = [0] * length

    for i in range(length):
        count[arr[i]] += 1

    for i in range(1, k):
        count[i] += count[i - 1]
    
    for i in range(length - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(length):
        arr[i] = output[i]

# Testing module
def testCountingSort():
    print('Testowanie sortowania przez zliczanie . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        countingSort(testing_list, 101)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testCountingSort()

if __name__ == '__main__':
    main()