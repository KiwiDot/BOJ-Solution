# 백준 32246번 빙고 막기
import sys
put = sys.stdin.readline

N = int(put())

print(N if N != 2 else N+1)