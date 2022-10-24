n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

d_sum = k
for i in range(n):
    d_sum -= abs(a[i] - b[i])
    
if (d_sum%2 == 0 and d_sum >= 0):
    print("Yes")
else:
    print("No")