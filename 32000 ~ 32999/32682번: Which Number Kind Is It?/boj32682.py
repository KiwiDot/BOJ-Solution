# 백준 32682번 Which Number Kind Is It?
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())
    answer = ""

    if N % 2:
        answer += "O"

    if N == int(N ** 0.5) ** 2:
        answer += "S"

    print(answer if answer else "EMPTY")