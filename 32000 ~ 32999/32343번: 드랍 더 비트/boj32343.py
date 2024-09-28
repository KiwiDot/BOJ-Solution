# 백준 32343번 드랍 더 비트
import sys
put = sys.stdin.readline

N = int(put())
a, b = map(int, put().split())

n = N * 2 - a - b if a + b > N else a + b
answer = '1' * n + '0' * (N - n)

print(int(answer, 2))