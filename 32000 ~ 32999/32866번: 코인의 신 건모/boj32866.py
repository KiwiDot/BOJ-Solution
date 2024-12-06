# 백준 32866번 코인의 신 건모
import sys
put = sys.stdin.readline

N = int(put())
X = int(put())

answer = (N * X * 100) / (N * (100 - X))
print(answer)


