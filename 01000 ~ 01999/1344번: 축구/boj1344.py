# 백준 1344번 축구
import sys
put = sys.stdin.readline

A = int(put())
B = int(put())
a, b = [1], [1]

for i in range(1, 19):
    ai = [j * (100 - A) / 100 for j in a] + [0]
    bi = [j * (100 - B) / 100 for j in b] + [0]

    for j in range(1, len(ai)):
        ai[j] += a[j-1] * A / 100
        bi[j] += b[j-1] * B / 100

    a = ai
    b = bi

A = B = 0
prime = {2, 3, 5, 7, 11, 13, 17}
for i in range(19):
    if i not in prime:
        A += a[i]
        B += b[i]

print(1 - A * B)