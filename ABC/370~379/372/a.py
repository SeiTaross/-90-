import sys
import io

_INPUT = """\
a.b.c.

"""

sys.stdin = io.StringIO(_INPUT)

S = input()

s = S.split(".")
for si in s:
    print(si, end="")
print()
