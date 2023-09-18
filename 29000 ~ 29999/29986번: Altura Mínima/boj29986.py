# 백준 29986번 Altura Mínima
import sys
put = sys.stdin.readline

N, H = map(int, put().split())
A = list(map(int, put().split()))

answer = sum([int(i <= H) for i in A])
print(answer)