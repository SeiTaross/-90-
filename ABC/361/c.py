import sys
import io

_INPUT = """\
5 2
3 1 5 4 9

"""

sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 10 ** 9
for i in range(K+1):
    ans = min(ans, A[i + (N - K) - 1] - A[i])

print(ans)