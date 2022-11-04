N, M = map(int, input().split())

ans = [0]*N
for i in range(M):
    a, b = map(int, input().split())
    if a > b:
        ans[a-1] += 1
    else:
        ans[b-1] += 1

print(ans.count(1))
