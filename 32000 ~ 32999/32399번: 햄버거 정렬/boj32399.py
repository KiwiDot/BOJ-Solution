# 백준 32399번 햄버거 정렬
import sys
put = sys.stdin.readline

S = put().strip()

match S:
    case '(1)':
        print(0)
    case ')1(':
        print(2)
    case _:
        print(1)