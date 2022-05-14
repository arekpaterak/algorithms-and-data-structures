# Arkadiusz Paterak - BUCKET SORT

import time
import random 

def createRandomListForBucket():
    size = random.randint(100, 1000)
    return [random.randint(0, 100) / 100 for _ in range(size)]

# The algorithm
def bucketSort(arr):
    length = len(arr)
    buckets = [[] for _ in range(length)]

    for num in arr:
        bucket = int(10 * num)
        buckets[bucket].append(num)
    
    for bucket in buckets:
        bucket.sort()

    arr.clear()

    for bucket in buckets:
        for num in bucket:
            arr.append(num)

# Testing module
def testBucketSort():
    print('Testowanie sortowania kubełkowego . . .')
    time.sleep(1)

    for _ in range(1000):
        testing_list = createRandomListForBucket()

        right_sort = sorted(testing_list)

        bucketSort(testing_list)

        if testing_list != right_sort:
            print('Algorytm sortowania nie działa poprawnie.')
            return

    print('Algorytm sortowania działa poprawnie.')

# The main body
def main():
    testBucketSort()

if __name__ == '__main__':
    main()