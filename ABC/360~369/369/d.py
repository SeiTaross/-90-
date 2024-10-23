import sys
import io

_INPUT = """\
5
1 5 3 2 7

"""

sys.stdin = io.StringIO(_INPUT)

def max_sum_with_conditions(N, A):
    # DPテーブルの初期化
    # dp[i][j] は i 番目まで処理して j 回目に追加した場合の最大合計
    dp = [[-float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][1] = A[0]  # 最初の要素を選ぶ場合
    
    for i in range(1, N):
        for j in range(1, i + 2):  # j 回目に追加する場合
            # 足さない場合
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            
            if j > 1:  # 足す場合
                if j % 2 == 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2 * A[i])
                else:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + A[i])
    
    # 最大値を求める
    return max(dp[N-1])

# 入力
N = int(input())
A = list(map(int, input().split()))

print(max_sum_with_conditions(N, A))




