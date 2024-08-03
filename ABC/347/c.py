import sys
import io

_INPUT = """\
3 3 4
5 6 7
"""

sys.stdin = io.StringIO(_INPUT)

N, A, B = map(int, input().split())
D = list(map(int, input().split()))

E = list(set([d % (A+B) for d in D]))
E.sort()

if E[-1] - E[0] < A:
    print("Yes")
    exit()

for i in range(len(E)-1):
    if E[i+1] - E[i] > B:
        print("Yes")
        exit()

print("No")
