# 백준 1342번 행운의 문자열
import sys
from collections import Counter
put = sys.stdin.readline


def solution(s, idx, n, N):
    if n == N:
        global answer
        answer += 1

    else:
        for i in range(s):
            if i == idx:
                continue
            if cnt[i]:
                cnt[i] -= 1
                solution(s, i, n+1, N)
                cnt[i] += 1


S = put().strip()
cnt = list(dict(Counter(S)).values())
answer = 0

solution(len(cnt), -1, 0, len(S))
print(answer)
