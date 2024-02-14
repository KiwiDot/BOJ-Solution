# 백준 1678번 기차
import sys
put = sys.stdin.readline

T, M, N = map(int, put().split())
train = ["" for i in range(60)]

for i in range(T):
    data = put().split()
    for j in data[1:-1]:
        train[int(j)] = data[0]

train = [i for i in train[M:] + train[:M] if i]
n = (N - 1) % len(train)
print(train[n])

