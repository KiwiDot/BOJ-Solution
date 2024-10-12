# 백준 32449번 Animal Farm
import sys
put = sys.stdin.readline

n = int(put())
species = []
pig = 0

while n:
    n -= 1
    s, i = put().split()

    if s == "pig":
        pig = max(pig, int(i))
    else:
        species += [int(i)]

answer = [i for i in species if i < pig]
print(pig + sum(answer))