import sys
import io

_INPUT = """\
< < >


"""

sys.stdin = io.StringIO(_INPUT)

ab, ac, bc = input().split()

ans = "C"
if ab == ">":
    if ac == "<":
        ans = "A"
    elif bc ==">":
        ans = "B"
else:
    if ac == ">":
        ans = "A"
    elif bc == "<":
        ans = "B"
        
print(ans)
    
        