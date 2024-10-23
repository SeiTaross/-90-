import sys
import io

_INPUT = """\
4 7
2 M
3 M
1 F
4 F
4 F
1 F
2 M

"""

sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())

born_boy = [0] * N
for i in range(M):
    A, B = input().split()
    A = int(A)
    if born_boy[A-1] == 0 and B == "M":
        print("Yes")
        born_boy[A-1] = 1
    else:
        print("No")
    
    