# 백준 32371번 샷건
import sys
put = sys.stdin.readline

keyboard = {}
for i in range(4):
    k = put().strip()
    for j in range(len(k)):
        keyboard[k[j]] = (i, j)

k = put().strip()
x = y = 0
for i in k:
    x += keyboard[i][0]
    y += keyboard[i][1]

x, y = x // 9, y // 9
for i in keyboard:
    if keyboard[i] == (x, y):
        print(i)
        break