# 백준 31533번 Furiosa AI 영상 처리 가속
import sys
put = sys.stdin.readline

a = int(put())
m, n = map(int, put().split())

answer = min(m * 2 / a, n * 2 / a, max(m / a, n), max(m, n / a))
print(answer)
