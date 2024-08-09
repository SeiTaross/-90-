import sys
import io

_INPUT = """\
133
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())

valid_nums = [0, 2, 4, 6, 8]

t = 0
while 5**(t+1) <= N:
    t += 1

idx = [0] * (t+1)
for i in range(t, -1, -1):
    n = (N-1) // (5**i)
    idx[i] = n
    N -= n*(5**i)

ans = 0
for i in range(t+1):
    ans += valid_nums[idx[i]] * (10**i)

print(ans)