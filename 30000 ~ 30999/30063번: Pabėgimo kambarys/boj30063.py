# 백준 30063번 Pabėgimo kambarys
import sys
put = sys.stdin.readline

N = int(put())
text = put().strip()
check = {'R': 0, 'A': 0, 'K': 0, 'T': 0, 'S': 0}

for i in range(N):
    if text[i] in check:
        check[text[i]] += 1

    if check['R'] and check['K'] and check['T'] and check['S'] and check['A'] > 1:
        print(i + 1)
        break