import sys
import io

_INPUT = """\
10 10 10 20 20 20
10 15 10 25 25 25
"""

sys.stdin = io.StringIO(_INPUT)

a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

if (not(g >= d  or j <= a)) and (not(h >= e or k <= b)) and (not(i >= f or l <= c)):
    print("Yes")
else:
    print("No")