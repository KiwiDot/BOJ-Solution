# 백준 32215번 코드마스터 2024
import sys
put = sys.stdin.readline

n, m, k = map(int, put().split())
answer = (k + 1) * m

print(answer)