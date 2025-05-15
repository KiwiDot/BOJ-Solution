# 백준 33574번 끊임없는 정렬과 창조함으로
import sys
put = sys.stdin.readline

Q = int(put())
S = []

while Q:
    Q -= 1
    data = list(map(int, put().split()))

    match data[0]:
        case 1:
            x = data[1]
            S = sorted(S) if x == 1 else sorted(S, reverse=True)
        case 2:
            x, t = data[1:]
            S.insert(x, t)

print(len(S))
print(*S)