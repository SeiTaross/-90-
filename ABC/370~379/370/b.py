import sys
import io

_INPUT = """\
6
2
1 5
1 6 3
2 6 1 4
2 1 1 1 6
5 6 1 2 2 5

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

ans = A[0][0]
for i in range(1,N):
    a = max(ans, i+1)
    b = min(ans, i+1)
    ans = A[a-1][b-1]

print(ans)