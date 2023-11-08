# 백준 30435번 Die Hard
import sys
put = sys.stdin.readline

d1 = list(map(int, put().split()))
d2 = list(map(int, put().split()))
d3 = list(map(int, put().split()))
cnt = [[0, 0], [0, 0], [0, 0]]
tie = [36, 36, 36]

for i in range(6):
    for j in range(6):
        if d1[i] > d2[j]:
            cnt[0][0] += 1
        elif d2[j] > d1[i]:
            cnt[1][1] += 1
        else:
            tie[0] -= 1

        if d2[i] > d3[j]:
            cnt[1][0] += 1
        elif d3[j] > d2[i]:
            cnt[2][1] += 1
        else:
            tie[1] -= 1

        if d3[i] > d1[j]:
            cnt[2][0] += 1
        elif d1[j] > d3[i]:
            cnt[0][1] += 1
        else:
            tie[2] -= 1

dice1 = [cnt[0][0] / tie[0] if tie[0] else 0,
         cnt[0][1] / tie[2] if tie[2] else 0, 1]
dice2 = [cnt[1][0] / tie[1] if tie[1] else 0,
         cnt[1][1] / tie[0] if tie[0] else 0, 2]
dice3 = [cnt[2][0] / tie[2] if tie[2] else 0,
         cnt[2][1] / tie[1] if tie[1] else 0, 3]

for i, j, n in [dice1, dice2, dice3]:
    if i >= 0.5 and j >= 0.5:
        print(n)
        break
else:
    print("No dice")