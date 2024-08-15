import sys
import io

_INPUT = """\
8
1 2 3 4 5 10 9 11

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

sort_A = sorted(A)

ans = A.index(sort_A[-2]) + 1
print(ans)
