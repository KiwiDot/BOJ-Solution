# 백준 32185번 꿈 열정 나눔
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
VPS = sum(list(map(int, put().split())))
member = []

for i in range(N):
    vps = sum(list(map(int, put().split())))
    if vps <= VPS:
        member.append((vps, i+1))

member.sort(reverse=True)
answer = [0] + [i for vps, i in member[:M-1]]

print(*answer)