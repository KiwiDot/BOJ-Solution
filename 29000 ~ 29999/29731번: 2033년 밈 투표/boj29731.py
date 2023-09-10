# 백준 29731번 2033년 밈 투표
import sys
put = sys.stdin.readline

N = int(put())
P = {"Never gonna give you up",
     "Never gonna let you down",
     "Never gonna run around and desert you",
     "Never gonna make you cry",
     "Never gonna say goodbye",
     "Never gonna tell a lie and hurt you",
     "Never gonna stop"}

S = {put().strip() for i in range(N)}

print("No" if S.issubset(P) else "Yes")