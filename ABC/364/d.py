import sys
import io

_INPUT = """\
10 5
-84 -60 -41 -100 8 -8 -52 -62 -61 -76
-52 5
14 4
-2 6
46 2
26 7

"""
        

sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
a = list(map(int, input().split()))
b = []
k = []
for i in range(Q):
    b_i, k_i = map(int, input().split())
    b.append(b_i)
    k.append(k_i)
    
for i in range(Q):
    C = a.copy()
    d = [abs(c - b[i]) for c in C]
    d.sort()
    print(d[k[i]-1])    

