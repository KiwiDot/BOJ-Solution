# 백준 32216번 찬물 샤워
import sys
put = sys.stdin.readline

n, k, T = map(int, put().split())
d = list(map(int, put().split()))

print(sum(d))