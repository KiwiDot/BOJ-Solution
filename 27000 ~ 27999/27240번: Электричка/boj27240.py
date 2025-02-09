# 백준 27240번 Электричка
import sys
put = sys.stdin.readline


n, a, b = map(int, put().split())
s, t = sorted(list(map(int, put().split())))

if a < s < t < b:
    print("City")

elif s < t <= a or b <= s < t:
    print("Outside")

else:
    print("Full")