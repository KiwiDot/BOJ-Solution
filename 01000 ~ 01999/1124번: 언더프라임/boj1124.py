# 백준 1124번 언더프라임
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
prime = []
check = [1] * (B+1)
check[1] = 0

for i in range(2, B+1):
    if check[i]:
        prime.append(i)

        for j in range(i*2, B+1, i):
            check[j] = 0

dp = [0] * (B + 1)
answer = 0

for i in range(2, B+1):
    for j in prime:
        if i % j == 0:
            dp[i] = dp[i // j] + 1
            break

    if A <= i <= B and check[dp[i]]:
        answer += 1

print(answer)