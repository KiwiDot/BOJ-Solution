# 백준 27252번 Пути Дика
import sys
put = sys.stdin.readline

text = put().strip()
x = h = 0
check = []

for i in text:
    match i:
        case "(":
            x += 1
            h = max(h, x)
            a = ["."] * h
            a[x-1] = "/"
            check.append(''.join(a[::-1]))

        case ")":
            x -= 1
            a = ["."] * h
            a[x] = "-"
            check.append(''.join(a[::-1]))

for i in range(len(check)):
    check[i] = check[i].rjust(h, ".")

answer = [['.'] * len(text) for i in range(h)]
for i in range(len(text)):
    for j in range(h):
        answer[j][i] = check[i][j]
        if answer[j][i] == '-':
            answer[j][i] = "\\"

for i in answer:
    print(''.join(i))