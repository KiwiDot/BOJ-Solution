# 백준 32307번 Injured Shoulder
import sys
put = sys.stdin.readline

n = int(put())
word = [put().strip() for i in range(n)]
word2 = set()

for i in word:
    for j in word:
        word2.add(i + j)

m = int(put())

while m:
    m -= 1
    w = put().strip()

    if w in word:
        print(1)
    elif w in word2:
        print(2)
    else:
        print(0)