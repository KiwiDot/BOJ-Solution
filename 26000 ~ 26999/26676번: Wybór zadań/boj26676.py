# 백준 26676번 Wybór zadań
import sys
put = sys.stdin.readline

n = int(put())
word = put().split()
check = {"5A": 0, "5B": 0, "5C": 0}
check2 = {}

for i in word:
    if i in check:
        check[i] += 1
    else:
        check2[i] = 1

if {0, 1} & set(check.values()) or len(check2) < 12:
    print("NIE")
else:
    print("TAK")