import sys
import io

_INPUT = """\
3
3 5
-4 1
-2 3

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
L =[]
R = []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

if sum(L) > 0 or sum(R) < 0:
    print("No")
    exit()

ans = L.copy()
sumA = sum(ans)
for i in range(N):
    ans[i] += min(-sumA, R[i] - L[i])
    sumA += min(-sumA, R[i] - L[i])

print("Yes")
print(*ans)