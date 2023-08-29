# 백준 16943번 숫자 재배치
import sys
put = sys.stdin.readline


def solution(num, n, N):
    global C
    d = N - n

    if n == N:
        if num[0] != '0' and int(num) < B:
            C = max(C, int(num))

    elif num and int(num) * 10 ** d > B:
        return 0

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                solution(num + a[i], n + 1, N)
                visited[i] = 0


A, B = map(int, put().split())
a, b = str(A), str(B)
visited = [0] * len(a)

C = -1
solution("", 0, len(a))
print(C)