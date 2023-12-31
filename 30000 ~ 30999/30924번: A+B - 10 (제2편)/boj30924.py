# 백준 30924번 A+B - 10 (제2편)
import sys
import random
put = sys.stdin.readline

answer = 0
for AB in ['A', 'B']:
    num = list(range(1, 10001))
    random.shuffle(num)
    for i in range(9999):
        print(f"? {AB} {num[i]}", flush=True)
        if int(put()):
            answer += num[i]
            break
    else:
        answer += num[-1]

print(f'! {answer}', flush=True)