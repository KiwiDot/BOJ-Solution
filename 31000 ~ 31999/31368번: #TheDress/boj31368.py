# 백준 31368번 #TheDress
import sys
put = sys.stdin.readline

N = int(put())
cnt = [0, 0, 0]

for i in range(N):
    answer = put().strip()

    if "blue" in answer and "black" in answer:
        cnt[0] += 1
    elif "white" in answer and "gold" in answer:
        cnt[1] += 1
    else:
        cnt[2] += 1

for i in cnt:
    print(i * 100 / N)