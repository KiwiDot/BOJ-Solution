# 백준 31090번 2023은 무엇이 특별할까?
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = put().strip()
    n = int(N[2:])

    print("Bye" if (int(N)+1) % n else "Good")