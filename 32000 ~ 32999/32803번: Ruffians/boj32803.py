# 백준 32803번 Ruffians
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    c1 = put().split()
    c2 = put().split()
    answer = "NO"

    for i in range(5):
        if c1[i] in c2[:i] + c2[i+1:]:
            answer = "YES"

    print(answer)