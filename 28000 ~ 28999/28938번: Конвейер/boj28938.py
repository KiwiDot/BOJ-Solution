# 백준 28938번 Конвейер
import sys
put = sys.stdin.readline

n = int(put())
num = sum(list(map(int, put().split())))

if num < 0:
    print("Left")
elif num > 0:
    print("Right")
else:
    print("Stay")