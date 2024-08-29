import sys
import io

_INPUT = """\
12
ssskkyskkkky

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(input())

alpha = set()
for s in S:
    alpha.add(s)

ans = {}
for a in alpha:
    ans[a] = 0

count = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        count += 1
    else:
        ans[S[i]] = max(ans[S[i]], count)
        count = 1
ans[S[-1]] = max(ans[S[-1]], count)

total = 0
for a in alpha:
    total += ans[a]

print(total)