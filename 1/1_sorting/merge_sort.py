# Arkadiusz Paterak - MERGE SORT

import time

from random_list import createRandomList

# The algorithm - merge sort
def mergeSort(arr, start, end):
    if start < end:
        middle = (start + end) // 2

        mergeSort(arr, start, middle)
        mergeSort(arr, middle + 1, end)
        merge(arr, start, middle, end)

def merge(arr, start, middle, end):
    left_lenght = middle - start + 1
    right_lenght = end - middle
    
    left_arr = []
    right_arr = []

    for i in range(left_lenght):
        left_arr.append(arr[start + i])
    
    for j in range(right_lenght):
        right_arr.append(arr[middle + 1 + j])

    i = 0
    j = 0
    k = start
  
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
  
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Testing module
def testMergeSort():
    print('Testowanie sortowania przez scalanie . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomList()

        right_sort = sorted(testing_list)

        mergeSort(testing_list, 0, len(testing_list) - 1)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testMergeSort()

if __name__ == '__main__':
    main()