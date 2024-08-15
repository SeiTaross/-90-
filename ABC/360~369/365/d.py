import sys
import io

_INPUT = """\
24
SPRPSRRRRRPPRPRPSSRSPRSS

"""

sys.stdin = io.StringIO(_INPUT)

def get_winning_hand(hand):
    if hand == 'R':
        return 'P'
    elif hand == 'P':
        return 'S'
    elif hand == 'S':
        return 'R'

N = int(input())
S = list(input())

ans = 1
prev_hand = get_winning_hand(S[0])
for i in range(1, N):
    current_hand = get_winning_hand(S[i])
    if current_hand == prev_hand:
        current_hand = S[i]
    else:
        ans += 1
    
    prev_hand = current_hand

print(ans)