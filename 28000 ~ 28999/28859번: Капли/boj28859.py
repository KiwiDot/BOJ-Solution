# 백준 28859번 Капли
import sys
put = sys.stdin.readline

n, m, k = map(int, put().split())
p = list(map(int, put().split()))

d = sum([m // i for i in p])
answer = k // m * d

d = sum([(k % m) // i for i in p])
answer += d

print(answer)
