# 백준 29830번 Mägedes sõitmine
import sys
put = sys.stdin.readline

N = int(put())
H = list(map(int, put().split()))
D = list(map(int, put().split()))

h = H.pop(0)
answer = []

for i in range(N):
    h += D[i]
    if h == H[i]:
        answer.append('M')
    elif h > H[i]:
        answer.append('V')
    else:
        answer.append('T')

print(''.join(answer))