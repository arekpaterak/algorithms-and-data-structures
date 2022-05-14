# Arkadiusz Paterak - program testujący wszystkie algorytmy (wystarczy go włączyć)

from quick_sort import testQuickSort
from heap_sort import testHeapSort
from counting_sort import testCountingSort
from radix_sort import testRadixSort
from bucket_sort import testBucketSort

import time  

def testAll():
    ''' One test to rule them all '''
    tests = [testQuickSort, testHeapSort, testCountingSort, testRadixSort, testBucketSort]

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