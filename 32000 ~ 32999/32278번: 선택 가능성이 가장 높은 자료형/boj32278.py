# 백준 32278번 선택 가능성이 가장 높은 자료형
import sys
put = sys.stdin.readline

N = int(put())

if -2 ** 15 <= N < 2 ** 15:
    print("short")

elif -2 ** 31 <= N < 2 ** 31:
    print("int")

else:
    print("long long")