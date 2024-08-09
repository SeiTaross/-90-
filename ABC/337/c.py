import sys
import io

_INPUT = """\
30
3 25 20 6 18 12 26 1 29 -1 21 17 23 9 8 30 10 15 22 27 4 13 5 11 16 24 28 2 19 7

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

B = {}
for i in range(N):
    B[A[i]] = i+1

ans = []
ans.append(B[-1])
for i in range(1, N):
    ans.append(B[ans[i-1]])

print(*ans)