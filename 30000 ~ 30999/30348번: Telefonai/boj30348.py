# 백준 30348번 Telefonai
import sys
put = sys.stdin.readline

N = int(put())
num = []

while N:
    N -= 1
    K = list(put().strip())

    if len(set(K)) == 1 or (len(set(K)) == len(K) and K == sorted(K)):
        num.append(int(''.join(K)))

print(min(num) if num else "NERASTA")