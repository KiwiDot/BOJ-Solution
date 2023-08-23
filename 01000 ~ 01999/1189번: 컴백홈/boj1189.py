# 백준 1189번 컴백홈
import sys
put = sys.stdin.readline


def solution(r, c, k):
    global R, C, K
    if k == K and r == 0 and c == C - 1:
        global answer
        answer += 1

    else:
        for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= i < R and 0 <= j < C and data[i][j] == '.':
                data[i][j] = 'T'
                solution(i, j, k+1)
                data[i][j] = '.'


R, C, K = map(int, put().split())
data = [list(put().strip()) for i in range(R)]
data[R-1][0] = 'T'
answer = 0

solution(R-1, 0, 1)
print(answer)