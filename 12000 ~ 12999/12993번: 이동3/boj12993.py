# 백준 12993번 이동3
import sys
put = sys.stdin.readline

x, y = map(int, put().split())

# x3: 3진수 표기
x3 = ""
while x:
    x, r = divmod(x, 3)
    x3 += str(r)
x3 = x3[::-1]

# y3: 3진수 표기
y3 = ""
while y:
    y, r = divmod(y, 3)
    y3 += str(r)
y3 = y3[::-1]

length = max(len(x3), len(y3))
x3 = x3.zfill(length)
y3 = y3.zfill(length)

for i in range(length):
    if int(x3[i]) + int(y3[i]) != 1:
        print(0)
        break
else:
    print(1)