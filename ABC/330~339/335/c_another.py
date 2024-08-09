import sys
import io

_INPUT = """\
5 9
2 3
1 U
2 3
1 R
1 D
2 3
1 L
2 1
2 5

"""

sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
d = [(i+1, 0) for i in range(N)][::-1]

for i in range(Q):
    T, C = input().split()
    if T == '1':
        x, y = d[-1]
        if C == 'U': y += 1
        if C == 'D': y -= 1
        if C == 'R': x += 1
        if C == 'L': x -= 1
        d.append((x, y))
    else:
        print(*d[-int(C)])