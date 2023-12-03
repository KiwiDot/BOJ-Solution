# 백준 30821번 별자리가 될 수 있다면
import sys
put = sys.stdin.readline

N = int(put())
answer = N * (N-1) * (N-2) * (N-3) * (N-4) // 120

print(answer)