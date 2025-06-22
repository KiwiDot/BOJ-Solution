# 백준 22477번 Kagisys
import sys
put = sys.stdin.readline

n = int(put())
ids = {put().strip() for i in range(n)}

m = int(put())
q = [put().strip() for i in range(m)]

check = True
for i in q:
    if i in ids:
        if check:
            print("Opened by", i)
            check = False
        else:
            print("Closed by", i)
            check = True
    else:
        print("Unknown", i)
