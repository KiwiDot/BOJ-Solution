# 백준 32403번 전구 주기 맞추기
import sys
put = sys.stdin.readline

N, T = map(int, put().split())
a = list(map(int, put().split()))

t = {i for i in range(1, T+1) if T % i == 0}
answer = 0

for i in a:
    diff = min([abs(i - j) for j in t])
    answer += diff

print(answer)