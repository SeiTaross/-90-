import sys
import io

_INPUT = """\
19
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())

num = ["1" * (i+1) for i in range(12)]

sums = set()
for i in range(12):
    for j in range(12):
        for k in range(12):
           sums.add(int(num[i]) + int(num[j]) + int(num[k]))

sums = list(sums)
sums.sort()

print(sums[N-1])