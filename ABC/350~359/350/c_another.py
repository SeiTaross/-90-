import sys
import io

_INPUT = """\
8
2 8 4 6 1 3 5 7

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

A = [a-1 for a in A]
ans = []
for i in range(N):
    while A[i] != i:
        ans.append((i+1, A[i]+1))
        tmp = A[A[i]]
        A[A[i]] = A[i]
        A[i] = tmp

print(len(ans))
for i in ans:
    print(*i)