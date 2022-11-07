from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

for i in range(Q):
    B = int(input())
    x = bisect_left(A, B)
    if x == 0:
        print(abs(A[0] - B))
    elif x == N:
        print(abs(A[N-1] - B))
    else:
        print(min(abs(A[x] - B), abs(A[x-1] - B)))
    
    