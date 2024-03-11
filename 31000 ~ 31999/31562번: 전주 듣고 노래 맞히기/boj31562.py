# 백준 31562번 전주 듣고 노래 맞히기
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
song = {}

while N:
    N -= 1
    data = put().split()
    T, S, a = data[0], data[1], ''.join(data[2:][:3])
    song[S] = a

while M:
    M -= 1
    b = ''.join(put().split())
    answer = []

    for i in song:
        if song[i] == b:
            answer.append(i)

    match len(answer):
        case 0:
            print('!')
        case 1:
            print(answer[0])
        case _:
            print('?')