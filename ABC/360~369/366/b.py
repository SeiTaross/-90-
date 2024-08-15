import sys
import io

_INPUT = """\
3
atcoder
beginner
contest

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = []
l = []
for i in range(N):
    s = list(input())
    S.append(s)
    l.append(len(s))

for j in range(max(l)):
    T = ""
    for i in range(N-1, -1, -1):
        if l[i] >= j+1:
            T += S[i][j]
        else:
            T += "*"
    while T[-1] == "*":
        T = T[:-1]
    print(T)
