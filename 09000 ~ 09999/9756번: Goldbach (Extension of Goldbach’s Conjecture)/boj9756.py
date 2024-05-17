# 백준 9756번 Goldbach (Extension of Goldbach’s Conjecture)
import sys
put = sys.stdin.readline

while True:
    m = int(put())
    if not m:
        break

    A = 'Y'
    B = m * (m - 1) + 1
    print(A, B)