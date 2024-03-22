# 백준 31663번 Mean Words
import sys
put = sys.stdin.readline

N = int(put())
word = [put().strip() for i in range(N)]
answer = ""

for i in range(max([len(j) for j in word])):
    w = 0
    n = 0

    for j in word:
        if i < len(j):
            w += ord(j[i])
            n += 1

    answer += chr(w // n)

print(answer)