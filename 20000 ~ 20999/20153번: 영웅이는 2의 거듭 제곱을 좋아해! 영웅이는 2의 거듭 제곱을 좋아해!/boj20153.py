# 백준 20153번 영웅이는 2의 거듭 제곱을 좋아해! 영웅이는 2의 거듭 제곱을 좋아해!
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
a = 0

for i in A:
    a ^= i

answer = {a}
for i in A:
    answer.add(a ^ i)

print(f"{max(answer)}{max(answer)}")