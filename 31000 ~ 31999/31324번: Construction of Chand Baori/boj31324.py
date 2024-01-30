# 백준 31324번 Construction of Chand Baori
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
cnt = 1

for i in range(N):
    cnt *= 2 * (i+1)

print("Harshat Mata" if cnt >= M else "Nope")