# 백준 33488번 아름다운 수열
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())
    print("YES")
    print(*[i for i in range(1, N+1)])
