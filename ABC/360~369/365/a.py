import sys
import io

_INPUT = """\
1900

"""

sys.stdin = io.StringIO(_INPUT)

Y = int(input())

ans = 365
if Y % 4 == 0:
    if Y % 100 != 0: 
        ans = 366
    else:
        if Y % 400 != 0:
            ans = 365
        else:
            ans = 366

print(ans)