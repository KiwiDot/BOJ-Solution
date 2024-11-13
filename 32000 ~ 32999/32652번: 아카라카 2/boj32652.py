# 백준 32652번 아카라카 2
import sys
put = sys.stdin.readline


K = int(put())
answer = "AKARAKA" + "RAKA" * (K - 1)

print(answer)