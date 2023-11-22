# 백준 30404번 오리와 박수치는 춘배
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
X = list(map(int, put().split()))

answer = 0
clap = 0
for i in X:
    if clap >= i:
        pass
    else:
        clap = i + K
        answer += 1

print(answer)