# 백준 29410번 Дома
import sys
put = sys.stdin.readline

N, a, b = map(int, put().split())
cnt = {'0': 0, '1': 0}

while N:
    N -= 1
    c = list(map(int, put().split()))

    for i in c[1:]:
        for j in bin(i)[2:]:
            cnt[j] += 1

answer = cnt['0'] * a + cnt['1'] * b
print(answer)