# 백준 30282번 Paskaitos
import sys
put = sys.stdin.readline

data = {1: [], 2: [], 3: [], 4: [], 5: []}
dup = []
answer = 0

for i in range(10):
    s, hpr, mpr, hpb, mpb = map(int, put().split())
    pr = hpr * 60 + mpr
    pb = hpb * 60 + mpb

    check = ""
    t = {j for j in range(pr, pb)}
    for j, tj in data[s]:
        if t & tj:
            check = f"{j + 1} {i + 1}"
            break

    if check:
        print("NE")
        print(check)
        break

    data[s].append((i, t))
    answer += len(t)

else:
    print("TAIP")
    h, m = divmod(answer, 60)
    print(h, m)