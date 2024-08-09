import sys
import io

_INPUT = """\
4 3 7
2 3 5 11

"""

sys.stdin = io.StringIO(_INPUT)

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = A[:K] + [X] + A[K:]

print(*ans)