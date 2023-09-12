# 백준 29724번 🍎📦 '사과상자'에 들어있는 것은 무엇? 현금?
import sys
put = sys.stdin.readline

N = int(put())
A = B = 0
cnt = 0

while N:
    N -= 1
    T, W, H, L = put().split()
    if T == 'A':
        w = int(W) // 12
        h = int(H) // 12
        l = int(L) // 12
        A += w * h * l
        cnt += 1

    else:
        B += 50

print(A * 500 + B * 120 + cnt * 1000)
print(A * 4000)