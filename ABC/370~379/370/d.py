import sys
import io

_INPUT = """\
4 3 10
2 2
4 1
1 1
4 2
2 1
3 1
1 3
1 2
4 3
4 2

"""

sys.stdin = io.StringIO(_INPUT)

H, W, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

walls = [[1 * W] * H]
