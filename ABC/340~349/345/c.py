import sys
import io

_INPUT = """\
abcdeee
"""

sys.stdin = io.StringIO(_INPUT)

S = list(input())
