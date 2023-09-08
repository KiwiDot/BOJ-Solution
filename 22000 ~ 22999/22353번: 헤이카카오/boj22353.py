# 백준 22353번 헤이카카오
import sys
put = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution(time, r, k):
    if r >= 1:
        return time
    else:
        return time * r + (1 - r) * solution(time + a, r * k, k)


a, d, k = map(int, put().split())
answer = solution(a, d / 100, 1 + k / 100)

print(answer)
