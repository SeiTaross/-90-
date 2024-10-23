import sys
import io

_INPUT = """\
3
2 3 3

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
    t_amari = (T % 3) + 1 
    T += (h // 5) * 3
    remaining_hp = h % 5
    if t_amari == 1:
        if remaining_hp <= 2:
            T += remaining_hp 
        else:
            T += 3
    elif t_amari == 2:
        if remaining_hp <= 1:
            T += remaining_hp
        else:
            T += 2
    else:
        if 1 <= remaining_hp <= 3:
            T += 1
        else:
            T += 2
    
print(T)