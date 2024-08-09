import sys
import io

_INPUT = """\
10
1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num_a = [10**6]*N
for i in range(N):
    if A[i] != 0:
        num_a[i] = Q[i]//A[i]

min_a = min(num_a)

ans = []
for i in range(min_a+1):
    tmp_Q = Q.copy()
    for j in range(N):
        tmp_Q[j] -= A[j]*i

    num_b = [10**6]*N
    for j in range(N):
        if B[j] != 0:
            num_b[j] = tmp_Q[j]//B[j]
    min_b = min(num_b)

    ans.append(i+min_b)

print(max(ans))