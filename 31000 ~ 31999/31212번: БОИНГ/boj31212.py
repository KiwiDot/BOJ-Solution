# 백준 31212번 БОИНГ
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()

seat = ["1D", "1E", "1F"]

for i in range(2, 21):
    for j in ["A", "B", "C", "D", "E", "F"]:
        seat.append(str(i) + j)

seat += ["21D", "21E"]

if s in seat:
    seat.remove(s)

print(seat[n] if n < len(seat) else "full")