import sys
import io

_INPUT = """\
4
1 3 5 7
1 2 3 4
4
1 1
2 6
0 10
2 2


"""

sys.stdin = io.StringIO(_INPUT)
 
def cumulative_sum(N, X, P):
    cumsum = {}
    
    current_sum = 0
    cumsum[X[0]-1] = 0
    for i in range(N):
        current_sum += P[i]
        cumsum[X[i]] = current_sum
        
    return cumsum
 
def find_max_index_leq(arr, target):
    """
    ソートされた配列 arr に対して、target 以下の最大の値のインデックスを返す。
    target を超えない最大の要素を見つけます。

    :param arr: ソートされた配列
    :param target: 探索する最大値
    :return: target 以下の最大の値のインデックス。該当する要素がない場合は -1。
    """
    left, right = 0, len(arr) - 1
    result_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] <= target:
            result_index = mid  # arr[mid] は target 以下なので候補となる
            left = mid + 1  # より大きい値を探すために右側に進める
        else:
            right = mid - 1  # target 以下の要素を探すために左側に戻る
    
    return result_index

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())

cumsum = cumulative_sum(N, X, P)

for i in range(Q):
    L, R = map(int, input().split())
    L = max(X[0], L)
    L = X[find_max_index_leq(X, L)]
    R = min(X[-1], R)
    R = X[find_max_index_leq(X, R)]
    print(L, R)
    if L != X[0]:
        total_people = cumsum[R] - cumsum[L] 
    else:
        total_people = cumsum[R]
    print(total_people)

