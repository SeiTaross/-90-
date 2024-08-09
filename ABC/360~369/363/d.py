def solve(N):
    # 桁数を求める
    n = 0
    digits= 1
    while True:
        if digits == 1:
            nextDigitsN = 10
        elif digits == 2:
            nextDigitsN = n + 9
        else:
            nextDigitsN = n + 9 * (10 ** ((digits - 1) // 2))
        if nextDigitsN >= N:
            break
        else:
            n = nextDigitsN
            digits += 1

    # その桁数の何番目か
    left = N - n

    # 1桁の場合
    if digits == 1:
        return left - 1

    # 2桁の場合
    elif digits == 2:
        return left * 10 + left


    ans = [0 for _ in range(digits)]

    # 両端はプラス1する
    if
    ans[0] = ans[digits - 1] = left // (10 ** ((digits - 1) // 2)) + 1
    left %= (10 ** ((digits - 1) // 2))

    for i in range(1, (digits - 1) // 2):
        ans[i] = ans[digits - i - 1] = left // (10 ** ((digits - 2 * i - 1) // 2))
        left %= (10 ** ((digits - 2 * i - 1) // 2))

    # 真ん中はマイナス1する
    if left != 0:
        ans[digits // 2] = ans[digits - digits // 2 - 1] = left - 1
    else:
        ans[digits // 2] = ans[digits - digits // 2 - 1] = 9

    # 答えを整数値にする
    Ans = 0
    for i in range(len(ans)):
        Ans += ans[i] * (10 ** i)

    return Ans

# print(solve(29))
for i in range(1,1000):
	print(i, solve(i))