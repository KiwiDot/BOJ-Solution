# 백준 32751번 햄버거
import sys
put = sys.stdin.readline

N = int(put())
A, B, C, D = map(int, put().split())
S = put().strip()
check = True

s = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
s[S[0]] += 1

for i in range(1, N):
    if S[i] == S[i-1]:
        check = False
        break

    s[S[i]] += 1

if S[0] == S[-1] == 'a' and check and s['a'] <= A and s['b'] <= B and s['c'] <= C and s['d'] <= D:
    print("Yes")
else:
    print("No")