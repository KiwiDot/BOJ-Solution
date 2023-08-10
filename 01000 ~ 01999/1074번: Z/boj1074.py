# 백준 1074번 Z
import sys
put = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution(n, x, y, cnt):
    if n == 1:
        cnt += x * 2 + y
        return cnt

    else:
        cx = int(x >= 2 ** (n-1))
        cy = int(y >= 2 ** (n-1))
        c = 4 ** (n-1)

        cnt += cx * c * 2 + cy * c
        x %= 2 ** (n-1)
        y %= 2 ** (n-1)

        return solution(n-1, x, y, cnt)


N, r, c = map(int, put().split())
answer = solution(N, r, c, 0)
print(answer)