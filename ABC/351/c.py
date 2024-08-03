import sys
import io

_INPUT = """\
5
0 0 0 1 2

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

l = 0
ans = [0] * 200000
for i in range(N):
    ans[l] = A[i]
    l += 1
    while l > 1:
        if ans[l - 1] == ans[l - 2]:
            ans[l - 2] += 1
            l -= 1
        else:
            break

print(l)
