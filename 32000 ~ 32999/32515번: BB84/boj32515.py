# 백준 32515번 BB84
import sys
put = sys.stdin.readline

N = int(put())

VH1 = put().strip()
k1 = put().strip()

VH2 = put().strip()
k2 = put().strip()

idx = [i for i in range(N) if VH1[i] == VH2[i]]

v1 = [k1[i] for i in idx]
v2 = [k2[i] for i in idx]

if v1 == v2:
    print(''.join(v1))
else:
    print('htg!')