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

from collections import deque

N, Q = map(int, input().split())
query = [list(input().split()) for _ in range(Q)]

dragon = deque()
for i in range(1, N+1):
    dragon.append((i, 0))

for i in range(Q):
    if query[i][0] == '1':
        C = query[i][1]
        head_x = dragon[0][0]
        head_y = dragon[0][1]
        if C == 'U':
            head_y += 1
        elif C == 'D':
            head_y -= 1
        elif C == 'R':
            head_x += 1
        elif C == 'L':
            head_x -= 1
        dragon.pop()
        dragon.appendleft((head_x, head_y))

    else:
        p = int(query[i][1])
        print(*dragon[p-1])

