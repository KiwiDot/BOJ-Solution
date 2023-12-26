# 백준 31000번 교환 분배법칙
import sys
put = sys.stdin.readline

N = int(put())
answer = 0

for a in range(-N, N+1):
    if a == 0:
        # 0 + (b * c) = (b) * (c) 항상 성립한다
        answer += (N * 2 + 1) ** 2

    elif a < 0:
        # b + c = |a| + 1
        answer += N + (N + a)

    else:
        # b + c = -a + 1
        answer += N + (N - a + 2)

print(answer)