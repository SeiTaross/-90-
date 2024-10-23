import sys
import io

_INPUT = """\
1
1

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()
streak = 0
n = []
d = abs(A[0] - A[1])
for i in range(1, N-1):
    dn = abs(A[i]-A[i+1])
    if d == dn:
        streak += 1
        if streak == 1:
            l = i-1
    else:
        if streak >= 1:
            r = i
            n.append(r-l+1)
        streak = 0
    d = dn
if streak >= 1:
    r = N-1
    n.append(r-l+1)
    
ans = 2*N -1
for i in range(len(n)):
    ans += (n[i]-1)*(n[i]-2)//2

print(ans)