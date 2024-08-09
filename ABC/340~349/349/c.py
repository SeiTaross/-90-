import sys
import io

_INPUT = """\
arigato
ARA

"""

sys.stdin = io.StringIO(_INPUT)

S = input()
T = input().lower()

if T[2] == "x":
    a = S.find(T[0])
    b = S.find(T[1], a+1)
    if a != -1 and b != -1 and a < b:
        print("Yes")
    else:
        print("No")
else:
    a = S.find(T[0])
    b = S.find(T[1], a+1)
    c = S.find(T[2], b+1)
    if a != -1 and b != -1 and c != -1 and a < b < c:
        print("Yes")
    else:
        print("No")
