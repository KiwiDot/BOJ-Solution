# 백준 30021번 순열 선물하기
import sys
put = sys.stdin.readline

N = int(put())

if N == 2:
    print("NO")
else:
    print("YES")
    answer = [1, 3, 2, 4] + [i for i in range(5, N+1)]
    print(*answer[:N])