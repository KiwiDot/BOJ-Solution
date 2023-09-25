# 백준 30075번 Sveikas, Pasauli!
import sys
put = sys.stdin.readline

N = int(put())
answer = ""

while N:
    N -= 1
    data = put().split()

    answer += data[1][1:-1]

for i in answer.split("\\n"):
    print(i)
