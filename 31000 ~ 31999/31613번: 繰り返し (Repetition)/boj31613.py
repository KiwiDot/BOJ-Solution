# 백준 31613번 繰り返し (Repetition)
import sys
put = sys.stdin.readline

X = int(put())
N = int(put())
answer = 0

while X < N:
    answer += 1
    match X % 3:
        case 0:
            X += 1
        case 1:
            X *= 2
        case 2:
            X *= 3

print(answer)