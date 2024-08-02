import sys
import io

_INPUT = """\
345

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())

ans = 1
i = 1
while i**3 <= N:
    K = i ** 3
    s = str(K)
    if s == s[::-1]:
        ans = K
    i += 1

print(ans)