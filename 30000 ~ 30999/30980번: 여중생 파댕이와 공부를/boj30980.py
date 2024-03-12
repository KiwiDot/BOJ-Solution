# 백준 30980번 여중생 파댕이와 공부를
import sys
put = sys.stdin.readline

N, M = map(int, put().split())

while N:
    N -= 1
    data = [put().strip() for i in range(3)]
    answer = ['', '', '']

    for i in range(0, 8 * M, 8):
        if data[1][i+6].isdigit():
            solve = data[1][i+1:i+7].split('=')
            r = 1

        else:
            solve = data[1][i+1:i+6].split('=')
            r = 0

        if eval(solve[0]) == int(solve[1]):
            answer[0] += '.' + '*' * (r + 5) + '.' * (2 - r)
            answer[1] += '*' + '='.join(solve) + '*' + '.' * (1 - r)
            answer[2] += '.' + '*' * (r + 5) + '.' * (2 - r)
        else:
            d0 = list(data[0][i:i+8])
            d1 = list(data[1][i:i+8])
            d2 = list(data[2][i:i+8])
            d0[3] = d1[2] = d2[1] = '/'

            answer[0] += ''.join(d0)
            answer[1] += ''.join(d1)
            answer[2] += ''.join(d2)

    for i in answer:
        print(i)