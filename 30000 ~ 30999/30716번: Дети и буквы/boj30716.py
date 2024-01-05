# 백준 30716번 Дети и буквы
import sys
put = sys.stdin.readline

n = int(put())
string = put().strip()

for i in range(1, n):
    if string[0] != string[i]:
        print("Yes")
        print(1, i+1, 1)
        break
else:
    print("No")