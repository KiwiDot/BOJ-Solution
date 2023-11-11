# 백준 30665번 Pique Esconde
import sys
put = sys.stdin.readline

while True:
    n, m = map(int, put().split())
    if n == m == 0:
        break
    child = {i + 1 for i in range(n)} - {m} - {int(put()) for i in range(n - 2)}

    print(max(child))