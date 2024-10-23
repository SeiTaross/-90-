import sys
import io

_INPUT = """\
5
4
1 2
2 3
3 4
4 5
4
1 2
1 3
1 4
1 5
3 1 4 1
5 9 2
6 5
3

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
MG = int(input())
G = []
for i in range(MG):
    u, v = map(int, input().split())
    G.append((u, v))
MH = int(input())
H = []
for i in range(MG):
    u, v = map(int, input().split())
    H.append((u, v))
A = []
for i in range(N-1):
    A.append(list(map(int, input().split())))


    