# 백준 29756번 DDR 체력 관리
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
s = list(map(int, put().split()))
h = list(map(int, put().split()))

game = [[0] * 101 for i in range(N)]
game[0][100 - h[0]] = s[0]

for i in range(1, N):
    for j in range(101):
        hp1 = min(j + K, 100)
        hp2 = hp1 - h[i]

        game[i][hp1] = max(game[i][hp1], game[i-1][j])
        if hp2 >= 0:
            game[i][hp2] = max(game[i][hp2], game[i-1][j] + s[i])

print(max(game[-1]))