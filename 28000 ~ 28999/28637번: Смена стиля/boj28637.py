# 백준 28637번 Смена стиля
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    s = put().strip()
    answer = [""]

    for i in s:
        if i.isupper():
            answer.append(i.lower())
        else:
            answer[-1] += i

    if answer[0] == "":
        answer.pop(0)

    print('_'.join(answer))