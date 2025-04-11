# 백준 33781번 Diagnosis
import sys
put = sys.stdin.readline

n, m = map(int, put().split())

D = list(map(int, put().split()))[1:]
d = [set(put().split()[1:]) for i in range(n)]

check = {str(i) for i in range(1, m+1)}
for i in D:
    check = check - d[i-1]

print("no" if check else "yes")