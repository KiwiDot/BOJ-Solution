# 백준 31672번 특별한 케이크 (easy)
import sys
put = sys.stdin.readline

# swi's cake is missing!
msg = put().strip()

N = int(put())
data = [[list(map(int, put().split())) for i in range(3)] for j in range(N)]
answer = []

for i in range(N):
    check = {i + 1 for i in range(N)}

    for j in range(N):
        M = data[j][0][0]
        S = set(data[j][1])
        B = data[j][2][0]

        # i + 1번째 학생이 범인일 때
        if i == j:
            B ^= 1

        if B:
            check &= S
        else:
            check -= S

    # i + 1번째 학생이 용의자 리스트에 있어야 함
    if i + 1 in check:
        answer.append(i + 1)

if answer:
    print(*answer)
else:
    print("swi")