import numpy as np

N, K = input().split()
k = int(K)

for i in range(k):
    ans = 0
    mod = []
    digit = 0
    N = int(N, 8)
    while N > 0:
        mod.append(N % 9)
        digit += 1
        N = N // 9
    for j in range(digit):
        if mod[j] == 8:
            mod[j] = 5
        ans += mod[j] * 10**j
    N = str(ans)
            
print(ans)
