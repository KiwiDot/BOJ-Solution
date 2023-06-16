# 백준 5522번 카드 게임
import sys
put = sys.stdin.readline

answer = 0

for i in range(5):
    answer += int(put())

print(answer)
