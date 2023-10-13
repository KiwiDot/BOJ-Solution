# 백준 30020번 치즈버거 만들기 2
import sys
put = sys.stdin.readline

A, B = map(int, put().split())

for i in range(1, 101):
    if A - B == i and B >= i:
        print("YES")
        print(i)

        cnt = [B // i] * i
        for j in range(B % i):
            cnt[j] += 1

        cnt.sort()
        for j in cnt:
            print("ab" * j + "a")
        break

else:
    print("NO")