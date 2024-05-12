# 백준 31831번 과민성 대장 증후군
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = list(map(int, put().split()))
answer = stress = 0

for i in A:
    stress = max(stress + i, 0)
    if stress >= M:
        answer += 1

print(answer)