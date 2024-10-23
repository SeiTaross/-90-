import sys
import io

_INPUT = """\
59048
"""

sys.stdin = io.StringIO(_INPUT)

M = int(input())

N = 0
A = []
while M != 0:
    i = 0
    while 3**(i+1) <= M:
        i += 1
    M -= (3**i)
    A.append(i)
    N += 1

print(N)
print(*A)