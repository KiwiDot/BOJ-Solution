# 백준 29991번 Fatigue-Fighting Vacation
import sys
put = sys.stdin.readline

D, C, R = map(int, put().split())
Ci = [int(put()) for i in range(C)]
Ri = [int(put()) for i in range(R)]

d = D + sum(Ri)
answer = R
for i in Ci:
    if i <= d:
        d -= i
        answer += 1
    else:
        break

print(answer)