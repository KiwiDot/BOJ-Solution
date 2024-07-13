# 백준 29641번 Текст
import sys
put = sys.stdin.readline

k = int(put())
text = put().split()
idx = 0

while idx < len(text):
    t = text[idx]
    n = len(t)
    idx += 1

    while n < k and idx < len(text):
        if n + len(text[idx]) + 1 > k:
            break
        t += " " + text[idx]
        n += len(text[idx]) + 1
        idx += 1

    print(t)