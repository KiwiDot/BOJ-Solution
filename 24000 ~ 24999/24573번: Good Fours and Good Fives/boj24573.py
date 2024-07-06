# 백준 24573번 Good Fours and Good Fives
import sys
put = sys.stdin.readline

N = int(put())
answer = n = 0

while n * 4 <= N:
    if not (N - n * 4) % 5:
        answer += 1
    n += 1

print(answer)