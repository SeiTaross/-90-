import sys
import io

_INPUT = """\
10
68 3
17 2
99 2
92 4
82 4
10 3
100 2
78 1
3 1
35 4


"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = {}
for i in range(N):
    A, C = map(int, input().split())
    if C in ans:
        ans[C] = min(ans[C], A)
    else:
        ans[C] = A

print(max(ans.values()))


