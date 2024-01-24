# 백준 31282번 ЛОВНО КУЧЕ
import sys
from math import ceil
put = sys.stdin.readline

N, M, K = map(int, put().split())

diff = K - M
print(ceil(N / diff))