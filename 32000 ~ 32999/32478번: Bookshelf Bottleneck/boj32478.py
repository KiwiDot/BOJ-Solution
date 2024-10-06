# 백준 32478번 Bookshelf Bottleneck
import sys
put = sys.stdin.readline

n, H = map(int, put().split())
answer = 0

while n:
    n -= 1
    book = sorted(list(map(int, put().split())), reverse=True)

    for i in range(3):
        if book[i] <= H:
            answer += min(book[:i] + book[i+1:])
            break

    else:
        print("impossible")
        break

else:
    print(answer)