import sys
import io

_INPUT = """\
8 5
1 2 4 7 8


"""

sys.stdin = io.StringIO(_INPUT)

def cumulative_sum(arr, l, isReverse):
    cum_sum = [0] * l

    if isReverse:
        for i in range(l-1, -1, -1):
            cum_sum[i-1] = cum_sum[i] + arr[i]
    else:
        for i in range(l-1):
            cum_sum[i+1] = cum_sum[i] + arr[i]

    return cum_sum

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if K % 2 == 0:
    for i in range(0, K, 2):
       ans += (A[i+1] - A[i])
else:
    cum_sum = cumulative_sum(A, K, False)
    rev_cum_sum = cumulative_sum(A, K, True)
    weird_sum = []
    for i in range(1, K, 2):
        weird_sum.append(cum_sum[i-1] + rev_cum_sum[i-1])
    ans = min(weird_sum)

print(ans)
