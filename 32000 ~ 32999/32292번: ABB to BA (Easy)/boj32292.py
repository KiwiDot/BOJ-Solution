# 백준 32292번 ABB to BA (Easy)
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    S = put().strip()

    while "ABB" in S:
        S = S.replace("ABB", "BA", 1)

    print(S)