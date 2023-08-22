# 백준 16918번 봄버맨
import sys
put = sys.stdin.readline


def board(b1, b2):
    for i in range(R):
        for j in range(C):
            if b1[i][j] == 'O':
                b2[i][j] = '.'
                continue

            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < R and 0 <= jj < C and b1[ii][jj] == 'O':
                    b2[i][j] = '.'


R, C, N = map(int, put().split())
board1 = [list(put().strip()) for i in range(R)]
board2 = [['O'] * C for i in range(R)]
N -= 1

board3 = [['O'] * C for i in range(R)]
board(board1, board3)
board4 = [['O'] * C for i in range(R)]
board(board3, board4)

if not N:
    for i in board1:
        print(''.join(i))

else:
    answer = [board4, board2, board3, board2]
    for i in answer[N % 4]:
        print(''.join(i))