import sys
import io

_INPUT = """\
3 1
ABB
3 C

"""

sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
S = input()
count = S.count("ABC")
S = list(S)
for i in range(Q):
    X, C = input().split()
    X = int(X) - 1
    if S[X] == C:
        print(count)
        continue

    if S[X] == "A" and X <= N-2:
        if S[X+1] == "B" and S[X+2] == "C":
            count -= 1
    elif S[X] == "B" and 1 <= X <= N-2:
        if (S[X-1] == "A" and S[X+1] == "C"):
            count -= 1
    elif S[X] == "C" and X >= 2:
        if (S[X-2] == "A" and S[X-1] == "B"):
            count -= 1

    if C == "A" and X <= N-3:
        if S[X+1] == "B" and S[X+2] == "C":
            count += 1
    elif C == "B" and 1 <= X <= N-2:
        if S[X-1] == "A" and S[X+1] == "C":
            count += 1
    elif C == "C" and X >= 2:
        if S[X-2] == "A" and S[X-1] == "B":
            count += 1
            
    print(count)
    S[X] = C

