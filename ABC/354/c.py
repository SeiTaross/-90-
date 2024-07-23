import sys
import io

_INPUT = """\
3
2 4
1 1
3 2

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
cards = []
for i in range(N):
    A, C = map(int, input().split())
    cards.append([A, C])

tmp = sorted(cards, key=lambda x:x[1])

nowA = 0
ans = []
for i in range(N):
    if nowA < tmp[i][0]:
        ans.append()

print(cards)
