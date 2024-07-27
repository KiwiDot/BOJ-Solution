# 백준 29649번 Верное выражение
import sys
put = sys.stdin.readline

A, oprt, B, _, C = put().split()
answer = []

for i in range(2, 11):
    a = int(max(list(A)))
    b = int(max(list(B)))
    c = int(max(list(C)))

    if max(a, b, c) >= i:
        continue

    a = int(A, i)
    b = int(B, i)
    c = int(C, i)

    if eval(str(a) + oprt + str(b)) == c:
        answer.append(i)

print(len(answer))
print(*answer)