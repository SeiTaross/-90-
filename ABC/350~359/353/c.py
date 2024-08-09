import sys
import io

_INPUT = """\
3
3 50000001 50000002

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = 10 ** 8

sum = 0
for i in range(N):
    sum += (N-1) * A[i]

cnt = 0
idx = 0
for i in range(N):
    while (N - idx - 1 >= 0) and (A[i] + A[N - idx - 1] >= M):
        idx += 1
    cnt += idx
    if 2 * A[i] >= M:
        cnt -= 1

ans = sum - M * (cnt // 2)
print(ans)