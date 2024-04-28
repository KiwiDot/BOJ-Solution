# 백준 31490번 Throwing dice
import sys
put = sys.stdin.readline

M, N = map(int, put().split())
A = sum(list(map(lambda x: (int(x) + 1) / 2, put().split())))
B = sum(list(map(lambda x: (int(x) + 1) / 2, put().split())))

if A > B:
    print("ALICE")
elif A < B:
    print("BOB")
else:
    print("TIED")