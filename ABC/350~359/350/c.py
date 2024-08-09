import sys
import io

_INPUT = """\
3
3 1 2

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

A = [a-1 for a in A]
pos = [0] * N
for i in range(N):
    pos[A[i]] = i

ans = []
for i in range(N):
    if i != pos[i]:
        ans.append((pos[A[i]]+1, pos[i]+1))
        pos[A[i]] = pos[i]
        A[pos[i]] = A[i]
        A[i] = pos[i] = i

l = len(ans)
print(l)
for i in range(l):
    print(*ans[i])