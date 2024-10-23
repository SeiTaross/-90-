import sys
import io

_INPUT = """\
10 3
0 3 4 6 9 12 15 17 19 20

"""

sys.stdin = io.StringIO(_INPUT)

N, C = map(int, input().split())
T = list(map(int, input().split()))

ans = 1
t = T[0]
for i in range(1, N):
    if T[i] - t < C:
        continue
    else:
        ans += 1
        t = T[i]
print(ans)