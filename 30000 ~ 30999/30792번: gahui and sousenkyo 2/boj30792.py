# 백준 30792번 gahui and sousenkyo 2
import sys
put = sys.stdin.readline

n = int(put())
v1 = int(put())
v = list(map(int, put().split()))

answer = sorted(v + [v1], reverse=True).index(v1) + 1
print(answer)