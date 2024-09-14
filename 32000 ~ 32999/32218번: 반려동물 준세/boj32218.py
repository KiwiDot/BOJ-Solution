# 백준 32218번 반려동물 준세
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))
answer = 0

while True:
    answer += 1
    b = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if a[i] < a[j]:
                b[i] += 1

    if a == b:
        break
    a = b

print(answer)