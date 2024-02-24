# 백준 31416번 가상 검증 기술
import sys
put = sys.stdin.readline

Q = int(put())

while Q:
    Q -= 1
    Ta, Tb, Va, Vb = map(int, put().split())
    answer = 10 ** 6

    for i in range(Va+1):
        t1 = Ta * i + Tb * Vb
        t2 = Ta * (Va - i)

        if answer >= max(t1, t2):
            answer = max(t1, t2)
        else:
            break

    print(answer)