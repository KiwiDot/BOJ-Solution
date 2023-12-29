# 백준 30987번 하루 피부과
import sys
put = sys.stdin.readline

x1, x2 = map(int, put().split())
a, b, c, d, e = map(int, put().split())
func = []

for x in (x1, x2):
    func.append(a * x ** 3 // 3 + (b - d) * x ** 2 // 2 + (c - e) * x)

print(func[1] - func[0])