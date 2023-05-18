# 백준 1330번 두 수 비교하기
import sys
put = sys.stdin.readline

A, B = map(int, put().split())

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
