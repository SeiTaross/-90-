import sys
import io

_INPUT = """\
12
3 6 7 4 12 4 8 11 11 1 8 11
3925 9785 9752 3587 4013 1117 3937 7045 6437 6208 3391 6309


"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# 各要素の出現回数と重みの合計を管理するためのリスト
num = [0] * N
total_weight = [0] * N
max_weight = [0] * N

# 各要素の重みを集計
for i in range(N):
    num[A[i] - 1] += 1
    total_weight[A[i] - 1] += W[i]
    max_weight[A[i] - 1] = max(max_weight[A[i] - 1], W[i])

# 答えの初期化
ans = 0

# 各要素について処理
for i in range(N):
    if num[i] > 1:
        ans += (total_weight[i] - max_weight[i])

print(ans)