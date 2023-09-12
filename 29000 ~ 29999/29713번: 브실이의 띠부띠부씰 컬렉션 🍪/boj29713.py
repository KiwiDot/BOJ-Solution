# 백준 29713번 브실이의 띠부띠부씰 컬렉션 🍪
import sys
from collections import Counter
put = sys.stdin.readline

N = int(put())
alphabet = dict([(chr(i+65), 0) for i in range(26)])
BRONZESILVER = dict(Counter("BRONZESILVER"))

n = put().strip()
for i in n:
    alphabet[i] += 1

answer = set()
for i in BRONZESILVER:
    answer.add(alphabet[i] // BRONZESILVER[i])

print(min(answer))