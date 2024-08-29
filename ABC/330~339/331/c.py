import sys
import io

_INPUT = """\
50
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

a = sorted(A)
last_added = -1
sum_a = sum(a)
sums = {}
for i in range(N-1):
    if a[i] == a[i+1]:
        continue
    else:
        sub = a[i] * (i - last_added)
        sum_a -= sub
        sums[a[i]] = sum_a
        last_added = i
sums[a[-1]] = 0

for num in A:
    print(sums[num], end=" ")
print("")