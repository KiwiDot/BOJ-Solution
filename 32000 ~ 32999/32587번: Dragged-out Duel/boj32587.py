# 백준 32587번 Dragged-out Duel
import sys
put = sys.stdin.readline
rsp = {'R': 0, 'S': 1, 'P': 2}

n = int(put())
p1 = put().strip()
p2 = put().strip()
answer = 0

for i in range(n):
    p1i, p2i = rsp[p1[i]], rsp[p2[i]]

    if p1i - p2i in {2, -1}:
        answer += 1
    elif p1i == p2i:
        answer += 0
    else:
        answer -= 1

if answer > 0:
    print("victory")
else:
    print("defeat")