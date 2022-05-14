# Arkadiusz Paterak - COUNTING SORT

from random import randint
import time

def createList4Radix(d):
    length = randint(100, 1000)

    list = []
    for _ in range(length):
        num = 0
        for j in range(d):
            num += randint(0, 9) * (10 ** j)
        list.append(num)
    return list

# The algorithm
def radixSort(arr, d):
    for i in range(d):
        countingSortForRadix(arr, 101, i)

def countingSortForRadix(arr, k, position):
    length = len(arr)
    count = [0] * k
    output = [0] * length

    for i in range(length):
        index = arr[i] // (10 ** position) 
        count[index % 10] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for i in range(length - 1, -1, -1):
        index = arr[i] // (10 ** position)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(length):
        arr[i] = output[i]

# Testing module
def testRadixSort():
    print('Testowanie sortowania pozycyjnego . . .')
    time.sleep(1)

    for _ in range(1000):
        d = 5

        testing_list = createList4Radix(d)

        right_sort = sorted(testing_list)

        radixSort(testing_list, d)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testRadixSort()

if __name__ == '__main__':
    main()