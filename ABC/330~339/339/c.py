import sys
import io

_INPUT = """\
6
1 -2 3 4 -1 3

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans = max(ans+a, 0)

print(ans)