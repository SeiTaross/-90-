import sys
import io

_INPUT = """\
4
5 4 3 2
5 4 3

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

cnt = 0
for i in range(N):
    if i == N-1 and cnt == 0:
        ans = A[i]
        continue
    if A[i] > B[i-cnt]:
        cnt += 1
        ans = A[i]
        if cnt == 2:
            print(-1)
            exit()
print(ans)