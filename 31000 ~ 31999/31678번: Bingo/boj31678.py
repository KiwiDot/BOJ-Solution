# 백준 31678번 Bingo
import sys
put = sys.stdin.readline

n = int(put())
player = {}

while n:
    n -= 1
    name = put().strip()

    data = [put().split() for i in range(5)]
    garo = [set(i) for i in data]
    sero = [{data[i][j] for i in range(5)} for j in range(5)]
    diagonal = [{data[i][i] for i in range(5)}, {data[i][4 - i] for i in range(5)}]

    player[name] = garo + sero + diagonal

m = int(put())
number = set(put().split())
answer = []

for name in player:
    for bingo in player[name]:
        if len(bingo - number) == 0:
            answer.append(name)
            break

print(len(answer))
for i in answer:
    print(i)