import sys
import io

_INPUT = """\
998244353

"""

sys.stdin = io.StringIO(_INPUT)

import math

D = int(input())

# x の初期値設定と探索範囲の決定
x = 1
while (x + 1)**2 <= D:
    x += 1

# 初期値を D に設定
ans = D

# x の範囲を広げて探索
for i in range(x + 10):  # +10 で探索範囲を広げる
    tmp = D - i**2
    if tmp < 0:
        ans = min(ans, -tmp)
    else:
        y1 = int(math.isqrt(tmp))  # 平方根の整数部分を計算
        y2 = y1 + 1
        ans = min(ans, abs(tmp - y1**2), abs(y2**2 - tmp))

print(ans)