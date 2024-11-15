# 백준 32661번 Airfare Grants
import sys
put = sys.stdin.readline

N = int(put())
P = [int(put()) for i in range(N)]

answer = max(0, min(P) - max(P) // 2)

print(answer)