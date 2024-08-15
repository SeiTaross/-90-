import sys
import io

_INPUT = """\
8
1 2
1 2
3
2 2
1 4
1 4
2 2
3

"""

sys.stdin = io.StringIO(_INPUT)

Q = int(input())

box = {}
for i in range(Q):
    q = input()
    if len(q) != 1:
        q, x = map(int,q.split())
    if q == 1:
        if x in box:
            box[x] += 1
        else:
            box[x] = 1
    elif q == 2:
        box[x] -= 1
        if box[x] == 0:
            del box[x]
    else:
        print(len(box))