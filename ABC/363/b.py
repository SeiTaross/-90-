import sys
import io

_INPUT = """\
3 10 1
1 2 3

"""

sys.stdin = io.StringIO(_INPUT)

N, T, P = map(int, input().split())
L = list(map(int, input().split()))

L.sort()

if sum([l >= T for l in L]) >= P:
    print(0)
    exit()
else:
    print(T - L[-P])        