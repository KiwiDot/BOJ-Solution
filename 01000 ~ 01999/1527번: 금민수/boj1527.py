# 백준 1527번 금민수
import sys
put = sys.stdin.readline
change = {'0': '4', '1': '7'}

A, B = map(int, put().split())
a, b = len(str(A)), len(str(B))

cnt_A = sum([2 ** i for i in range(a)]) - 1
for i in range(2 ** a):
    n = int(''.join([change[j] for j in bin(i)[2:].zfill(a)]))
    if n > A:
        break
    cnt_A += 1

cnt_B = sum([2 ** i for i in range(b)]) - 1
for i in range(2 ** b):
    n = int(''.join([change[j] for j in bin(i)[2:].zfill(b)]))
    if n > B:
        break
    cnt_B += 1

answer = cnt_B - cnt_A
if set(str(A)).issubset({'4', '7'}):
    answer += 1

print(answer)
