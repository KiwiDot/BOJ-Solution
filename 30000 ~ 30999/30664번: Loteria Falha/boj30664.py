# 백준 30664번 Loteria Falha
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break

    if n % 42:
        print("TENTE NOVAMENTE")
    else:
        print("PREMIADO")