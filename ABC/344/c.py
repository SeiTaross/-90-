import sys
import io

_INPUT = """\
3
1 2 3
2
2 4
6
1 2 4 8 16 32
4
1 5 10 50

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))

sumABC = set()
for a in A:
    for b in B:
        for c in C:
            sumABC.add(a+b+c)

Q = int(input())
X = list(map(int, input().split()))

for x in X:
    if x in sumABC:
        print("Yes")
    else:
        print("No")