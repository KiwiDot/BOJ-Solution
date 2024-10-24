# 백준 32289번 Max-Queen
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
answer = 0

if n > 2 and m > 2:
    answer += (n - 2) * (m - 2) * 8

answer += (m + n - 4) * 2 * 5 + 4 * 3
print(answer // 2)
