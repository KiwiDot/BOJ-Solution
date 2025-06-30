# 백준 6942번 9966
import sys
put = sys.stdin.readline

rotate = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

m = int(put())
n = int(put())
answer = 0

for i in range(m, n + 1):
    check = []
    for j in str(i)[::-1]:
        if j in rotate:
            check.append(rotate[j])

    if check == list(str(i)):
        answer += 1

print(answer)
