# 백준 3186번 소변기
import sys
put = sys.stdin.readline

K, L, N = map(int, put().split())
data = put().strip() + '0' * L

used = False
k = l = 0

record0 = []
record1 = []

for i in range(N + L):
    if data[i] == '1':
        k += 1
        l = 0
        if not used and k == K:
            used = True
            record1.append(i+1)

    else:
        l += 1
        k = 0
        if used and l == L:
            used = False
            record0.append(i+1)

if record0:
    for i in record0:
        print(i)
else:
    print("NIKAD")