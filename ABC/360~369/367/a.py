import sys
import io

_INPUT = """\
10 7 17

"""

sys.stdin = io.StringIO(_INPUT)

A, B, C = map(int, input().split())

if B > C:
    if C < A < B:
        print("Yes")
    else:
        print("No")

else:
    if B < A < C:
        print("No")
    else:
        print("Yes")