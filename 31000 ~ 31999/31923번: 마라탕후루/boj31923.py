# 백준 31923번 마라탕후루
import sys
put = sys.stdin.readline

N, P, Q = map(int, put().split())
A = list(map(int, put().split()))
B = list(map(int, put().split()))

if P > Q:
    PQ = P - Q
    check = "YES"
    answer = []
    for i in range(N):
        a, b = A[i], B[i]
        if b >= a and (b - a) % PQ == 0:
            answer.append((b - a) // PQ)
        else:
            check = "NO"
            break

elif P < Q:
    PQ = Q - P
    check = "YES"
    answer = []
    for i in range(N):
        a, b = A[i], B[i]
        if a >= b and (a - b) % PQ == 0:
            answer.append((a - b) // PQ)
        else:
            check = "NO"
            break

else:
    answer = []
    check = "YES"
    for i in range(N):
        a, b = A[i], B[i]
        if a == b:
            answer.append(0)
        else:
            check = "NO"
            break

print(check)
if check == "YES":
    print(*answer)
