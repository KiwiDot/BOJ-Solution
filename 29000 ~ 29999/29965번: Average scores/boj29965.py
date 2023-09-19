# 백준 29965번 Average scores
import sys
put = sys.stdin.readline

N = int(put())
cnt = {'M': [0, 0], 'J': [0, 0]}

while N:
    N -= 1
    n, P = put().split()
    cnt[n][0] += 1
    cnt[n][1] += int(P)

M = cnt['M'][1] / cnt['M'][0] if cnt['M'][0] else 0
J = cnt['J'][1] / cnt['J'][0] if cnt['J'][0] else 0

if M > J:
    print('M')
elif M < J:
    print('J')
else:
    print('V')