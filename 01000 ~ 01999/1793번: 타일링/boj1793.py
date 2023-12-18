# 백준 1793번 타일링
dp = [1, 1, 3]

while True:
    try:
        n = int(input())
        while len(dp) <= n:
            dp.append(dp[-2] * 2 + dp[-1])
        print(dp[n])

    except EOFError:
        break