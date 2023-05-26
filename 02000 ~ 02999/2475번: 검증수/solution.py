# 백준 2475번 검증수
import sys
put = sys.stdin.readline

n = list(map(lambda x: int(x) ** 2, put().split()))
answer = sum(n) % 10

print(answer)
