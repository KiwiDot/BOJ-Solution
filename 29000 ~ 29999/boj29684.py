# 백준 29684번 Which Team Should Receive the Sponsor Prize?
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break

    a = list(map(int, put().split()))
    a = sorted([[abs(2023 - a[i]), i + 1] for i in range(n)],key=lambda x: x[0])

    print(a[0][1])