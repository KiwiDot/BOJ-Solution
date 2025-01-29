# 백준 33246번 Integrity Overflow
import sys
put = sys.stdin.readline

n = int(put())
pw = put().strip()

while n:
    n -= 1
    p, check = put().split()

    if len(pw) != len(p):
        c = "DENIED"

    else:
        cnt = 0
        for i in range(len(p)):
            if pw[i] != p[i]:
                cnt += 1

        if cnt > 1:
            c = "DENIED"
        else:
            c = "ALLOWED"

    if check != c:
        print("INTEGRITY OVERFLOW")
        break

else:
    print("SYSTEM SECURE")
