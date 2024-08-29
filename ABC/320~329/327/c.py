import sys
import io

_INPUT = """\
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6

"""

sys.stdin = io.StringIO(_INPUT)

map = [list(map(int, input().split())) for _ in range(9)]

for h in range(9):
    nums = set()
    for w in range(9):
        nums.add(map[h][w])
    if len(nums) != 9:
        print("No")
        exit()

for w in range(9):
    nums = set()
    for h in range(9):
        nums.add(map[h][w])
    if len(nums) != 9:
        print("No")
        exit()

for h in range(0, 9, 3):
    for w in range(0, 9, 3):
        nums = set()
        for h_add in range(3):
            for w_add in range(3):
                nums.add(map[h+h_add][w+w_add])
        if len(nums) != 9:
            print("No")
            exit()

print("Yes")