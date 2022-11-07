import itertools 
n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i, j, k, l, m in itertools.combinations(a, 5):
    if i % p * j % p * k % p * l % p * m % p == q:
        ans += 1

print(ans) 