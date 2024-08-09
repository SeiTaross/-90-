import sys
import io

_INPUT = """\
6 6
1 1
.#####
######
######
######
######
######
RURLDLULLRULRDL

"""

sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S_i, S_j = map(int, input().split())
Glid = []
for i in range(H):
    Glid.append(list(input()))  
X = input()

for i in range(len(X)):
    y = S_i
    x = S_j
    move = X[i]
    if y-2 >= 0 and move == "U":
        if Glid[y-2][x-1] == ".":
            S_i -= 1
    elif y < H and move == "D":
        if Glid[y][x-1] == ".":
            S_i += 1
    elif x-2 >= 0 and move == "L":
        if Glid[y-1][x-2] == ".":
            S_j -= 1
    elif x < W and move == "R":
        if Glid[y-1][x] == ".":
            S_j += 1

print(S_i, S_j)
        
               