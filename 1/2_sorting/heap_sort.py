# Arkadiusz Paterak - HEAP SORT

import time

from random_list import createRandomList

# The algorithm
def heapSort(arr, n):
    buildMaxHeap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, 0, i)

def buildMaxHeap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, i, n)

def maxHeapify(arr, i, n):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i

    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, n)

# Testing module
def testHeapSort():
    print('Testowanie sortowania przez kopcowanie . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        heapSort(testing_list, len(testing_list))

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testHeapSort()

if __name__ == '__main__':
    main()