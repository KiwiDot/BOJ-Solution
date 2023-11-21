# 백준 30618번 donstructive
import sys
put = sys.stdin.readline

N = int(put())
answer_1 = []
answer_2 = []

for i in range(1, N+1, 2):
    if i == N:
        answer_1.append(i)
    elif i % 4 == 1:
        answer_1.append(i)
        answer_2.append(i+1)
    else:
        answer_1.append(i+1)
        answer_2.append(i)

print(*(answer_1 + answer_2[::-1]))