# 백준 33556번 Java String  Equals
import sys
put = sys.stdin.readline

A = put().strip()
B = put().strip()

if A == "null":
    print("NullPointerException")
    print("NullPointerException")

elif B == "null":
    print("false")
    print("false")

else:
    a = A.lower()
    b = B.lower()

    print(str(A == B).lower())
    print(str(a == b).lower())