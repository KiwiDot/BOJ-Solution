# 백준 30584번 Середина игры
import sys
put = sys.stdin.readline

A = int(put())
B = int(put())

tie = min(A, B)
a = (A - tie) // 2
b = (B - tie) // 2

if a * 2 + tie == A and b * 2 + tie == B:
    if tie > 1:
        print("Undefined")
    else:
        print(a)
        print(b)
        print(tie)
else:
    print("Error")