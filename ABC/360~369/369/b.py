import sys
import io

_INPUT = """\
8
22 L
75 L
26 R
45 R
72 R
81 R
47 L
29 R

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())

left = []
right = []
for i in range(N):
    A, S = input().split()
    A = int(A)
    if S == "L":
        left.append(A)
    else:
        right.append(A)

ans = 0        
for i in range(len(left)-1):
    d = abs(left[i]-left[i+1])
    ans += d

for j in range(len(right)-1):
    d = abs(right[j] - right[j+1])
    ans += d
    
print(ans)