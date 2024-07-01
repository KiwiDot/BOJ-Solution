# 백준 6526번 Ambiguous permutations
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break
    answer = "ambiguous"

    num = list(map(int, put().split()))
    for i in range(n):
        if num[num[i]-1] != i+1:
            answer = "not ambiguous"
            break

    print(answer)