# 백준 31229번 또 수열 문제야
import sys
put = sys.stdin.readline

N = int(put())
A = [2 * i + 1 for i in range(N)]
print(*A)