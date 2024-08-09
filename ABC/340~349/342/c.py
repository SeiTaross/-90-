import sys
import io

_INPUT = """\
34
supercalifragilisticexpialidocious
20
g c
l g
g m
c m
r o
s e
a a
o f
f s
e t
t l
d v
p k
v h
x i
h n
n j
i r
s i
u a

"""

sys.stdin = io.StringIO(_INPUT)

import string

N = int(input())
S = list(input())
Q = int(input())

replace_from = [char for char in string.ascii_lowercase]
replace_to = replace_from.copy()
for i in range(Q):
    c, d = input().split()
    for i in range(len(replace_to)):
        if replace_to[i] == c:
            replace_to[i] = d

replace = dict(zip(replace_from, replace_to))

ans = ""
for s in S:
    ans += replace[s]

print(ans)