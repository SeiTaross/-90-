import sys
import io

_INPUT = """\
4
sweet
salty
sweet
sweet

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())

eatAll = True
cnt = 0
for _ in range(N):
    if cnt == 2:
        eatAll = False
    S = input()
    if S == "sweet":
        cnt += 1
    else:
        cnt = 0

if eatAll:
    print("Yes")
else:
    print("No")