import sys
import io

_INPUT = """\
5 3
1 2 3 4 5

"""

sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = A[N-K:] + A[:N-K]
print(*ans)