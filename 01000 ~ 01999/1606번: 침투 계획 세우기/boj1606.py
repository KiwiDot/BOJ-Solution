# 백준 1606번 침투 계획 세우기
import sys
put = sys.stdin.readline

x, y = map(int, put().split())
answer = y + 1

for i in range(1, x + y + int(not bool(y))):
    answer += i * 6

print(answer)