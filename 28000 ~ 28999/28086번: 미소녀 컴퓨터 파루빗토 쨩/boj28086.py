# 백준 28086번 미소녀 컴퓨터 파루빗토 쨩
import sys
put = sys.stdin.readline

data = put().strip()
A, op, B = "", "", ""

for i in data:
    if not A:
        A += i
    elif i.isdigit() or op:
        if op:
            B += i
        else:
            A += i
    else:
        op += i

a = str(int(A, 8))
b = str(int(B, 8))
if op == '/':
    op = '//'

try:
    answer = eval(a + op + b)
    if answer >= 0:
        print(oct(answer)[2:])
    else:
        print('-' + oct(abs(answer))[2:])
except ZeroDivisionError:
    print("invalid")