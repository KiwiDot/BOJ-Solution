# 백준 12026번 BOJ 거리
import sys
put = sys.stdin.readline

dp = {'B': [], 'O': [], 'J': []}
N = int(put())
s = put().strip()

for i in range(N):
    if s[i] == 'B':
        if not dp['B']:
            dp['B'].append((0, 0))
        if not dp['J']:
            continue

        E = 10 ** 6
        for n, j in dp['J']:
            k = i - j
            E = min(E, n + k ** 2)
        dp['B'].append((E, i))

    elif s[i] == 'O':
        if not dp['B']:
            continue

        E = 10 ** 6
        for n, j in dp['B']:
            k = i - j
            E = min(E, n + k ** 2)
        dp['O'].append((E, i))

    else:
        if not dp['O']:
            continue

        E = 10 ** 6
        for n, j in dp['O']:
            k = i - j
            E = min(E, n + k ** 2)
        dp['J'].append((E, i))

    if i == N - 1:
        print(E)
        break
else:
    print(-1)