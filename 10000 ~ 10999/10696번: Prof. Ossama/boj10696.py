# 백준 10696번 Prof. Ossama
import sys
put = sys.stdin.readline

T = int(put())

for n in range(1, T+1):
    N, X = map(int, put().split())

    print(f"Case {n}: {N % X}")