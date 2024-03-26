# 백준 28217번 두 정삼각형
import sys
put = sys.stdin.readline


def rotation(A):
    a = []
    for i in range(N):
        a.append([])
        for j in range(N):
            if i <= j:
                a[-1].append(A[j][i])
    return a[::-1]


def mirror(A):
    a = []
    for i in A:
        a.append(i[::-1])

    return a


N = int(put())
A = [list(map(int, put().split())) for i in range(N)]
B = [list(map(int, put().split())) for i in range(N)]

a1 = rotation(A)
a2 = rotation(a1)
a3 = mirror(A)
a4 = mirror(a1)
a5 = mirror(a2)

answer = []
for a in [A, a1, a2, a3, a4, a5]:
    cnt = 0
    for i in range(N):
        for j in range(i+1):
            if a[i][j] != B[i][j]:
                cnt += 1

    answer.append(cnt)

print(min(answer))