# 백준 30889번 좌석 배치도
import sys
put = sys.stdin.readline

N = int(put())
answer = dict([(chr(i+65), ['.'] * 20) for i in range(10)])

while N:
    N -= 1
    data = put().strip()
    i, j = data[0], int(data[1:]) - 1

    answer[i][j] = 'o'

for i in answer:
    print(''.join(answer[i]))