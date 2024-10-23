import sys
import io

_INPUT = """\
1 1
"""

sys.stdin = io.StringIO(_INPUT)

L, R = map(int, input().split())

if L+R == 0 or L+R == 2:
    print("Invalid")
else:
    if L == 1:
        print("Yes")
    else:
        print("No")