# 백준 31866번 손가락 게임
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
check = {0, 2, 5}

if a in check and b in check:
    n = b - a
    if n == 0:
        print('=')
    elif 5 > n > 0 or n == -5:
        print('>')
    else:
        print('<')

elif a in check:
    print('>')

elif b in check:
    print('<')

else:
    print('=')