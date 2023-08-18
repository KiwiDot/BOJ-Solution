# 백준 2615번 오목
import sys
put = sys.stdin.readline

data = [put().split() for i in range(19)]
answer = False

for i in range(19):
    for j in range(19):
        if data[i][j] == '0':
            continue
        color = data[i][j]
        cnt = [1] * 4

        # 가로
        if j == 0 or data[i][j-1] != color:
            ii, jj = i, j + 1
            while 0 <= ii < 19 and 0 <= jj < 19 and data[ii][jj] == color:
                cnt[0] += 1
                jj += 1
        # 세로
        if i == 0 or data[i-1][j] != color:
            ii, jj = i + 1, j
            while 0 <= ii < 19 and 0 <= jj < 19 and data[ii][jj] == color:
                cnt[1] += 1
                ii += 1

        # 대각선1
        if i == 0 or j == 0 or data[i-1][j-1] != color:
            ii, jj = i + 1, j + 1
            while 0 <= ii < 19 and 0 <= jj < 19 and data[ii][jj] == color:
                cnt[2] += 1
                ii += 1
                jj += 1

        # 대각선2
        if i == 18 or j == 0 or data[i+1][j-1] != color:
            ii, jj = i - 1, j + 1
            while 0 <= ii < 19 and 0 <= jj < 19 and data[ii][jj] == color:
                cnt[3] += 1
                ii -= 1
                jj += 1

        if 5 in cnt:
            print(color)
            print(i + 1, j + 1)
            answer = True
            break

    if answer:
        break

else:
    print(0)