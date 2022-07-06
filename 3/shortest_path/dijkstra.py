import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(n, edges, s):
    # Write your code here
    visited = [False for _ in range(n + 1)]
    distance = [math.inf for _ in range(n + 1)]
    distance[s] = 0
    q = [(distance[s], s)]   
        
    while q:
        d, u = heapq.heappop(q)
        if visited[u]:
            continue
        visited[u] = True
        for edge in edges:
            if edge[0] == u:
                v = edge[1]
                w = edge[2]
                if not visited[v] and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(q, (distance[v], v))
            elif edge[1] == u:
                v = edge[0]
                w = edge[2]
                if not visited[v] and d + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(q, (distance[v], v))

    # cleaning
    distance.pop(s)
    distance.pop(0)
    distance = [d if d is not math.inf else -1 for d in distance]
                    
    return distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])
            
        edges = set()
        
        for _ in range(m):
            edges.add(tuple(map(int, sys.stdin.readline().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()