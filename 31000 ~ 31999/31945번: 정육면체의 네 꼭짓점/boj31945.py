# 백준 31945번 정육면체의 네 꼭짓점
import sys
put = sys.stdin.readline

S = {(0, 1, 4, 5), (0, 1, 2, 3), (0, 2, 4, 6),
     (1, 3, 5, 7), (4, 5, 6, 7), (2, 3, 6, 7)}

T = int(put())

while T:
    T -= 1
    a, b, c, d = sorted(list(map(int, put().split())))

    print("YES" if (a, b, c, d) in S else "NO")