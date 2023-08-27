# 백준 12101번 1, 2, 3 더하기 2
import sys
put = sys.stdin.readline


def solution(num, N):
    global n, k
    if N == n:
        k -= 1
        if k == 0:
            print('+'.join(num))
            return 0

    elif k > 0:
        for i in range(1, 4):
            if N + i <= n:
                solution(num + [str(i)], N + i)
                if not k:
                    break


n, k = map(int, put().split())
solution([], 0)
if k:
    print(-1)