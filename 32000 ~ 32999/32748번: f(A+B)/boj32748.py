# 백준 32748번 f(A+B)
import sys
put = sys.stdin.readline

n1 = {}
n2 = {}

n = put().split()
for i in range(10):
    n1[n[i]] = str(i)
    n2[str(i)] = n[i]

f_A, f_B = put().split()
A = ''.join([n1[i] for i in f_A])
B = ''.join([n1[i] for i in f_B])
A_B = str(int(A) + int(B))

answer = ''.join([n2[i] for i in A_B])

print(answer)