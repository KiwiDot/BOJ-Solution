# 백준 34001번 임스의 일일 퀘스트
import sys
put = sys.stdin.readline

L = int(put())

a = [[200, 210, 220],
     [210, 220, 225],
     [220, 225, 230],
     [225, 230, 235],
     [230, 235, 245],
     [235, 245, 250]]

b = [[260, 265, 270],
     [265, 270, 275],
     [270, 275, 280],
     [275, 280, 285],
     [280, 285, 290],
     [285, 290, 295],
     [290, 295, 300]]

for x in [a, b]:
    answer = []
    for i in x:
        cnt = 0
        if i[0] <= L:
            cnt += 500
        if i[1] <= L:
            cnt -= 200
        if i[2] <= L:
            cnt -= 200

        answer.append(cnt)
    print(*answer)