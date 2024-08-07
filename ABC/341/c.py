import sys
import io

_INPUT = """\
13 16 9
ULURDLURD
################
##..##.#..####.#
###.#..#.....#.#
#..##..#####.###
#...#..#......##
###.##.#..#....#
##.#####....##.#
###.###.#.#.#..#
######.....##..#
#...#.#.######.#
##..###..#..#.##
#...#.#.#...#..#
################

"""

sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
T = list(input())
S = [list(input()) for _ in range(H)]

def is_valid(y, x):
    for t in T:
        if t == "L" and x > 0:
            if S[y][x-1] == ".":
               x -= 1
            else:
                return False
        elif t == "R" and x < W-1:
            if S[y][x+1] == ".":
                x += 1
            else:
                return False
        elif t == "U" and y > 0:
            if S[y-1][x] == ".":
                y -= 1
            else:
                return False
        elif t == "D" and y < H-1:
            if S[y+1][x] == ".":
                y += 1
            else:
                return False

    return True


ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == '.':
            if is_valid(y, x):
                ans += 1

print(ans)