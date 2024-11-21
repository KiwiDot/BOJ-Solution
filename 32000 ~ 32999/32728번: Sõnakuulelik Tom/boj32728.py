# 백준 32728번 Sõnakuulelik Tom
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
color = put().strip()
A, B, C = [], [], []

for i in color:
    if i == 's':
        if len(A) < K:
            A.append(i)
        elif len(B) < K:
            B.append(i)
        else:
            C.append(i)

    elif i == 'r':
        if len(B) < K:
            B.append(i)
        elif len(C) < K:
            C.append(i)
        else:
            A.append(i)

    else:
        if len(C) < K:
            C.append(i)
        elif len(A) < K:
            A.append(i)
        else:
            B.append(i)

print(''.join(A))
print(''.join(B))
print(''.join(C))