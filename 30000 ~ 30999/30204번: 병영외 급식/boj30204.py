# 백준 30204번 병영외 급식
import sys
put = sys.stdin.readline

N, X = map(int, put().split())
p = list(map(int, put().split()))

print(int(not sum(p) % X))