import math

a, b, c = map(int, input().split())

gcd_ab = math.gcd(a, b)
gcd_abc = math.gcd(gcd_ab, c)

ans = a//gcd_abc + b//gcd_abc + c//gcd_abc - 3

print(ans)