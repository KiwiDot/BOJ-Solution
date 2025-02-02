# 백준 33192번 Divar’s Salaries
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    x, k, h = map(int, put().split())
    k2 = 0
    k -= h

    if k > 140:
        k2 = k - 140
        k = 140

    a = str(k * x + k2 * x * 15 // 10 + h * x * 2)[::-1]
    answer = ""

    for i in range(0, len(a), 3):
        answer += a[i:i+3]
        if i < len(a) - 3:
            answer += ','

    print(answer[::-1])