# 백준 31922번 이 대회는 이제 제 겁니다
import sys
put = sys.stdin.readline

A, P, C = map(int, put().split())
answer = max(A + C, P)

print(answer)