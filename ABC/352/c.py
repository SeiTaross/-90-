import sys
import io

_INPUT = """\
10
690830957 868532399
741145463 930111470
612846445 948344128
540375785 925723427
723092548 925021315
928915367 973970164
563314352 832796216
562681294 868338948
923012648 954764623
691107436 891127278

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
B = []
maxd = 0
idx = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    d = b - a
    if maxd < d:
        maxd = d
        idx = i

A.pop(idx)
head = B.pop(idx)
sholders = sum(A)

print(head + sholders)


