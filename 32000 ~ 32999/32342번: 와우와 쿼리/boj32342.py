# 백준 32342번 와우와 쿼리
import sys
put = sys.stdin.readline

Q = int(put())

while Q:
    Q -= 1
    S = put().strip()
    answer = 0

    for i in range(len(S)):
        if S[i:i+3] == "WOW":
            answer += 1

    print(answer)