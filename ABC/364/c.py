import sys
import io

_INPUT = """\
8 30 30
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1

"""

sys.stdin = io.StringIO(_INPUT)

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sort_A = sorted(A.copy(), reverse=True)
sort_B = sorted(B.copy(), reverse=True)

sumA = 0
sumB = 0
for i in range(N):
    sumA += sort_A[i]
    sumB += sort_B[i]
    if sumA > X or sumB > Y:
        print(i+1)
        exit()
else:
    print(N)