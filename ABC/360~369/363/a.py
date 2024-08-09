import sys
import io

_INPUT = """\
250
"""

sys.stdin = io.StringIO(_INPUT)

R = int(input())

print(100 - R%100)