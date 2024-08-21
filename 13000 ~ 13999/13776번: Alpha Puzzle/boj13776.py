# 백준 13776번 Alpha Puzzle
import sys
put = sys.stdin.readline

S = int(put())
text = [put().strip() for i in range(S)]
answer = ""

for i in text:
    for j in i:
        if j != ' ' and j not in answer:
            answer += j

print(answer)