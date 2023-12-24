# 백준 31009번 진주로 가자! (Easy)
import sys
put = sys.stdin.readline

N = int(put())
data = {}

while N:
    N -= 1
    D, C = put().split()
    data[D] = int(C)

print(data["jinju"])
print(sum([1 for i in data if data[i] > data["jinju"]]))