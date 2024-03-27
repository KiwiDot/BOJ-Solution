# 백준 31694번 Kto wygrał?
import sys
put = sys.stdin.readline

Algosia = list(map(int, put().split()))
Bajtek = list(map(int, put().split()))

A = dict([(i, 0) for i in range(11)])
for i in Algosia:
    A[i] += 1

B = dict([(i, 0) for i in range(11)])
for i in Bajtek:
    B[i] += 1

if sum(Algosia) == sum(Bajtek):
    for i in range(10, 0, -1):
        if A[i] > B[i]:
            print("Algosia")
            break
        elif A[i] < B[i]:
            print("Bajtek")
            break
    else:
        print("remis")

elif sum(Algosia) > sum(Bajtek):
    print("Algosia")
else:
    print("Bajtek")