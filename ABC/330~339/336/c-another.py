import sys
import io

_INPUT = """\
31415926535

"""

sys.stdin = io.StringIO(_INPUT)

# 問題を言い換える

N = int(input()) - 1

digit = []
while N > 0:
    digit.append(N % 5)
    N //= 5

ans = 0
for i in range(len(digit)):
    ans += digit[i] * (10**i) * 2

print(ans)