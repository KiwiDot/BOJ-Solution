# 백준 32357번 더블팰린드롬
import sys
put = sys.stdin.readline

N = int(put())
cnt = 0

while N:
    N -= 1
    s = put().strip()

    # X나 Y가 될 수 있는 조건 = s가 팰린드롬이여야 한다
    if s == s[::-1]:
        cnt += 1

print(cnt * (cnt - 1))