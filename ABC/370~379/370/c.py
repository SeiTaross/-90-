import sys
import io

_INPUT = """\
adbe
bcbc

"""

sys.stdin = io.StringIO(_INPUT)

S = list(input())
T = list(input())

l = len(S)

if S == T:
    print(0)
    exit()
   
ans = []
flag = False 
for i in range(l):
    if S[i] > T[i]:
        S[i] = T[i]
        ans.append(S.copy())

for i in range(l-1, -1, -1):
    if S[i] != T[i]:
        S[i] = T[i]
        ans.append(S.copy())

print(len(ans))
for a in ans:
    print(*a, sep="")
