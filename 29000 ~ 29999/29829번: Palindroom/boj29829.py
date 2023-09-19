# 백준 29829번 Palindroom
import sys
put = sys.stdin.readline

num = list(map(int, put().split()))

if len(num) % 2:
    mun = num[:len(num)//2] + [num[len(num)//2]] + num[:len(num)//2][::-1]
else:
    mun = num[:len(num)//2] + num[:len(num)//2][::-1]

cnt = 0
for i in range(len(num)):
    cnt += int(num[i] != mun[i])

if cnt <= 1:
    print("JAH")
    print(*mun)

else:
    print("EI")