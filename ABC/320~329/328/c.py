import sys
import io

_INPUT = """\
5 1
aaaaa
1 5

"""

sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
S = list(input())

comulative_S = [0] * N
for i in range(1, N):
    if S[i] == S[i-1]:
        comulative_S[i] = comulative_S[i-1] + 1
    else:
        comulative_S[i] = comulative_S[i-1]

for i in range(Q):
    l, r = map(int, input().split())
    print(comulative_S[r-1]-comulative_S[l-1])
