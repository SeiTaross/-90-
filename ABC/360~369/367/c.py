import sys
import io

_INPUT = """\
5 5
2 3 2 3 2

"""

sys.stdin = io.StringIO(_INPUT)

from itertools import product

def generate_numbers_with_limits(n, k, limits):
    # 各桁ごとの最大値を定義したリスト
    if len(limits) != n:
        raise ValueError("The length of limits must be equal to the number of digits (n).")
    
    # 各桁の数字の範囲を設定
    digit_ranges = [range(1, limit + 1) for limit in limits]
    
    # 全ての組み合わせを生成
    for combination in product(*digit_ranges):
        # 結果を連結して文字列として表示
        ans = list(map(int, combination))
        if sum(ans) % k == 0:
            print(*ans)


N, K = map(int, input().split())
R = list(map(int, input().split()))

generate_numbers_with_limits(N, K, R)

     