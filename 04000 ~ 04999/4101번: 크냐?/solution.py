# 백준 4101번 크냐?
import sys
put = sys.stdin.readline

while True:
    a, b = map(int, put().split())
    if a == b == 0:
        break
        
    print("Yes" if a > b else "No")
