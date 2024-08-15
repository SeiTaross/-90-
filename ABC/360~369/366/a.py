import sys
import io

_INPUT = """\
99 12 50

"""

sys.stdin = io.StringIO(_INPUT)

N, T, A = map(int, input().split())

n = N // 2

if n < T or n < A:
    print("Yes")
else:
    print("No")