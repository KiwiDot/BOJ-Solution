# 백준 33674번 하늘에서 떨어지는 N개의 별
import sys
put = sys.stdin.readline

N, D, K = map(int, put().split())
s = list(map(int, put().split()))
cnt = [0] * N

answer = 0
while D:
    D -= 1
    check = False
    for i in range(N):
        cnt[i] += s[i]
        if cnt[i] > K:
            check = True

    if check:
        answer += 1
        cnt = s.copy()

print(answer)