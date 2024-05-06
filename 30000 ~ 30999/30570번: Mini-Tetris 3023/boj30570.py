# 백준 30570번 Mini-Tetris 3023
import sys
put = sys.stdin.readline

a, b, c = map(int, put().split())
answer = a * 2

if c >= 2:
    answer += b * 2 + 3
    c -= 2

answer += c // 2 * 3

print(answer)