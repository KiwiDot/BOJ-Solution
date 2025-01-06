# 백준 33016번 Problem C
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    S = list(put().strip())

    for i in range(len(S)):
        if S[i] != 'c':
            continue

        if i == len(S) - 1:
            S[i] = 'k'

        elif S[i+1] in {'e', 'i', 'y'}:
            S[i] = 's'

        elif S[i+1] == 'h':
            S[i] = 'c'
            S[i+1] = ''

        else:
            S[i] = 'k'

    if S[-1] == 'c':
        S[-1] = 'k'

    print(''.join(S))