# 백준 30032번 알파벳 뒤집기
import sys
put = sys.stdin.readline

solution = {'d': {1: 'q', 2: 'b'},
            'b': {1: 'p', 2: 'd'},
            'q': {1: 'd', 2: 'p'},
            'p': {1: 'b', 2: 'q'}}

N, D = map(int, put().split())

while N:
    N -= 1
    s = put().strip()

    print(''.join([solution[i][D] for i in s]))