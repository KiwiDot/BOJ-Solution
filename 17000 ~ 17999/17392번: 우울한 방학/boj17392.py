# 백준 17392번 우울한 방학
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
if N == 0:
    print(sum((i + 1) ** 2 for i in range(M)))
else:
    H = list(map(int, put().split()))
    h = max(M - sum(H) - N, 0)

    d = [h // (N + 1)] * (N + 1)
    for i in range(h % (N + 1)):
        d[i] += 1

    answer = sum([i * (i + 1) * (2 * i + 1) // 6 for i in d])
    print(answer)