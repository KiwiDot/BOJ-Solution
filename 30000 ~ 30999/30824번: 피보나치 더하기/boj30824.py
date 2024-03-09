# 백준 30824번 피보나치 더하기
import sys
from itertools import combinations_with_replacement
put = sys.stdin.readline

T = int(put())
F = [1, 1]

while F[-1] < 10 ** 16:
    F.append(F[-1] + F[-2])

while T:
    T -= 1
    k, x = map(int, put().split())

    for idx in range(len(F)):
        if F[idx] > x:
            break
    else:
        idx = len(F)

    f = {sum(i) for i in combinations_with_replacement(F[:idx], k)}

    print("YES" if x in f else "NO")