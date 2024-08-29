import sys
import io

_INPUT = """\
2 1
01

"""

sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = list(input().split("0"))

maxT = 0
for s in S:
    meal = s.count("1")
    pr = s.count("2")
    if meal > M:
        pr += (meal-M)

    maxT = max(pr, maxT)

print(maxT)
