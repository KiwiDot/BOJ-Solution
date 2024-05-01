# 백준 9184번 신나는 함수 실행
import sys
put = sys.stdin.readline

w = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

for i in range(21):
    for j in range(21):
        w[0][i][j] = w[0][j][i] = w[i][0][j] = w[j][0][i] = w[i][j][0] = w[j][i][0] = 1

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b < c:
                w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
            else:
                w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

while True:
    a, b, c = map(int, put().split())
    if a == b == c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        answer = 1

    elif a > 20 or b > 20 or c > 20:
        answer = w[20][20][20]
    else:
        answer = w[a][b][c]

    print(f"w({a}, {b}, {c}) = {answer}")