h, w = map(int, input().split())

if h == 1 or w == 1:
    print(max(h,w))
else:
    print(((h + 1) // 2) * ((w + 1) // 2))