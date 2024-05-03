# 백준 29598번 Два формата
import sys
put = sys.stdin.readline

N = int(put())
n256 = []

while N:
    N, r = divmod(N, 256)
    n256.append(r)

answer = 0
for i in n256:
    answer = answer * 256 + i

print(answer)