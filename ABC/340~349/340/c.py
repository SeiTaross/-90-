import sys
import io

_INPUT = """\
100000000000000000

"""

sys.stdin = io.StringIO(_INPUT)

from functools import cache

@cache
def f(N):
    if N == 1:
        return 0
    else:
        return f(N//2) + f((N+1)//2) + N

N = int(input())
ans = int(f(N))
print(ans)