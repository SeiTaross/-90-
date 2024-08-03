import sys
import io

_INPUT = """\

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
