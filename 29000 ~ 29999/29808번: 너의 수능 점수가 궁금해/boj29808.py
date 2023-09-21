# 백준 29808번 너의 수능 점수가 궁금해
import sys
put = sys.stdin.readline

S = int(put())
answer = []

# i는 국어, 영어의 표준점수 차 / j는 수학, 탐구의 표준점수 차
for i in range(201):
    for j in range(201):
        case = [i*508 + j*212, i*108 + j*212, i*508 + j*305, i*108 + j*305]
        for k in case:
            if k * 4763 == S:
                answer.append([i, j])
                break

print(len(answer))
for i in answer:
    print(*i)
