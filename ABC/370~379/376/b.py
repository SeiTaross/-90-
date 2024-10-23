import sys
import io

_INPUT = """\
100 2
L 1
R 2

"""

sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
queries = []
for i in range(Q):
    H, T = input().split()
    queries.append((H, int(T)))
    
L = 1
R = 2

ans = 0
for h, t in queries:
    d = 0
    reverse = False
    if h == 'L':
        while t != L:
            L = (L % N) + 1
            d += 1
            if L == R:
                reverse = True
        if reverse:
            d = N - d
        
    else:
        while t != R:
            R = (R % N) + 1
            d += 1
            if L == R:
                reverse = True
        if reverse:
            d = N - d
    ans += d

print(ans)