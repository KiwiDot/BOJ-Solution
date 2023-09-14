# 백준 29270번 그래서 님 푼 문제 수가?
import sys
put = sys.stdin.readline

N, M, K = map(int, put().split())

n = M * K
minimum = max(0, N - n)
maximum = max(0, N - M * (K-1) - 1)

print(minimum, maximum)