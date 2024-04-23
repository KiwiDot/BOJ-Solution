# 백준 7218번 Pasislėpę romėniški skaičiai
import sys
put = sys.stdin.readline

num = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12}
answer = []
N = int(put())
text = put().strip()

for i in num:
    if i in text:
        answer.append(num[i])

print(*answer)