# 백준 30868번 개표
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    n = int(put())
    answer = ['++++'] * (n // 5) + ['|' * (n % 5)]
    print(*answer)