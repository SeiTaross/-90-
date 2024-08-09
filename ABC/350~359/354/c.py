import sys
import io

_INPUT = """\
6
32 101
65 78
2 29
46 55
103 130
52 40

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
cards = []
for i in range(N):
    A, C = map(int, input().split())
    cards.append([A, C, i+1])

tmp = sorted(cards, key=lambda x:x[1])

maxA = 0
cnt = 0
ans = []
for i in range(N):
    if maxA < tmp[i][0]:
        maxA = tmp[i][0]
        cnt += 1
        ans.append(tmp[i][2])

ans.sort()
print(cnt)
print(*ans)
