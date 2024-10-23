import sys
import io

_INPUT = """\
9 5
9 9 8 2 4 4 3 5 3


"""

sys.stdin = io.StringIO(_INPUT)

def count_paths_with_sum_modulo_cycle(n, m, edge_weights):
    # 累積和の計算
    prefix_sum = [0] * (2 * n)
    for i in range(2 * n):
        prefix_sum[i] = edge_weights[i % n] + (prefix_sum[i - 1] if i > 0 else 0)
    
    # 剰余のカウント
    remainder_count = [0] * m
    total_count = 0
    
    for i in range(n):
        for length in range(1, n + 1):  # Path lengths from 1 to n
            end = i + length - 1
            path_sum = prefix_sum[end] - (prefix_sum[i - 1] if i > 0 else 0)
            if path_sum % m == 0:
                total_count += 1
    
    return total_count

# 入力の読み込み
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
edge_weights = list(map(int, data[2:]))

# 結果の取得
result = count_paths_with_sum_modulo_cycle(N, M, edge_weights)
print(result)



