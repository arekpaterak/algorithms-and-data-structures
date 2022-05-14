# Arkadiusz Paterak - program testujący wszystkie algorytmy (wystarczy go włączyć)

from linear_search import testLinearSearch
from binary_search import testBinarySearch
from bubble_sort import testBubbleSort
from insert_sort import testInsertSort
from selection_sort import testSelectionSort
from merge_sort import testMergeSort

import time  

def testAll():
    ''' One test to rule them all '''
    tests = [testLinearSearch, testBinarySearch, testBubbleSort, testInsertSort, testSelectionSort, testMergeSort]

    print('Rozpoczęto testowanie . . .\n')
    for test in tests:
        time.sleep(1)
        start = time.time()
        test()
        end = time.time()
        print(f'Czas wykonia 1000 testów algorytmu: {end - start} s.\n')

    time.sleep(1)

def main():
    testAll()

if __name__ == '__main__':
    main()