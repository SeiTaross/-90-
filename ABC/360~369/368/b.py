import sys
import io

_INPUT = """\
4
1 2 3 3

"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

import heapq

# もし全てが 0 だった場合はすぐに 0 を返す
if N == 1:
    print(0)
    exit()

# マイナスのヒープを作成する
A = [-x for x in A]
heapq.heapify(A)

ans = 0
while len(A) > 1:
    # 最大値を2つ取り出す
    largest = -heapq.heappop(A)
    second_largest = -heapq.heappop(A)
    
    # 最大値を減少させて再度ヒープに追加
    if largest > 1:
        heapq.heappush(A, -(largest - 1))
    if second_largest > 1:
        heapq.heappush(A, -(second_largest - 1))
    
    ans += 1

print(ans)
