# 백준 1141번 접두사
import sys
put = sys.stdin.readline

N = int(put())
word = sorted([put().strip() for i in range(N)])
X = [word[0]]

for i in word[1:]:
    if i.startswith(X[-1]):
        X[-1] = i
    else:
        X.append(i)

print(len(X))