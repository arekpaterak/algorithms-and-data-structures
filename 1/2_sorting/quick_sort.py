# Arkadiusz Paterak - QUICK SORT

import time

from random_list import createRandomList

# The algorithm
def quickSort(arr, p, r):
    if p < r:
        pivot = hoarePartition(arr, p, r)
        quickSort(arr, p, pivot) # dla zwykłego partision: pivot - 1
        quickSort(arr, pivot + 1, r)

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def hoarePartition(arr, p, r):
    pivot = arr[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while  arr[j] > pivot:
            j -= 1

        i += 1
        while arr[i] < pivot:
            i += 1
        
        if i < j:
            print(f"({i}, {j})")
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j

# Testing module
def testQuickSort():
    print('Testowanie sortowania szybkiego . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        quickSort(testing_list, 0, len(testing_list) - 1)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    # testQuickSort()
    a = [45, 7, 26, 15, 10, 30, 37, 5, 31, 17]
    quickSort(a, 0, 9)

if __name__ == '__main__':
    main()