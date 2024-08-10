import sys
import io

_INPUT = """\
10 23
2 5 6 5 2 1 7 9 7 2

"""

sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))

def maximize_subsidy_limit(A, M):
    low, high = 0, max(A)
    best_x = 0
    
    while low <= high:
        mid = (low + high) // 2
        total_cost = sum(min(mid, cost) for cost in A)
        
        if total_cost <= M:
            best_x = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return best_x

sum_a = sum(A)
if sum_a <= M:
    print("infinite")
    exit()

result = maximize_subsidy_limit(A, M)
print(result)

    
    