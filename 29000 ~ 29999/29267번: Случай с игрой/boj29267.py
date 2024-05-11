# 백준 29267번 Случай с игрой
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
save = m = 0

while n:
    n -= 1
    move = put().strip()

    match move:
        case "save":
            save = m
        case "load":
            m = save
        case "shoot":
            m = max(0, m-1)
        case "ammo":
            m += k

    print(m)