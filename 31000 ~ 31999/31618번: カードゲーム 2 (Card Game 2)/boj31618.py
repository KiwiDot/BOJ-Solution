# 백준 31618번 カードゲーム 2 (Card Game 2)
import sys
put = sys.stdin.readline

N = int(put())
A = set(map(int, put().split()))

for i in A:
    if i + 3 in A and i + 6 in A:
        print("Yes")
        break
else:
    print("No")