# 백준 11729번 하노이 탑 이동 순서
import sys
put = sys.stdin.readline
answer = []


def hannoi(N, A, C, B):
    if N == 1:
        answer.append((A, B))

    else:
        hannoi(N - 1, A, B, C)
        answer.append((A, B))
        hannoi(N - 1, C, A, B)


N = int(put())
hannoi(N, 1, 2, 3)

K = len(answer)
print(K)
for i in answer:
    print(*i)